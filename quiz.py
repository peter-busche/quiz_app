import hashlib
import json
import re
import textwrap
import threading
import webbrowser
from datetime import datetime
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).parent.resolve()
QUIZ_DIR = ROOT / "quizzes"
METRICS_DIR = ROOT / "metrics"
METRICS_LOCK = threading.Lock()
PORT = 8000

NUMBERED = re.compile(r"^\s*-\s*(\d+)\.[ \t]*(.*)$")
SECTION = re.compile(r"^\s*-?\s*###\s*(Questions|Answers|Wrong Answers):\s*$", re.I)
REFERENCE = re.compile(r"^\s*(\[[^\]]*\]\([^)]*\)|https?://)")
NOTE = re.compile(r"^\s*[-*]\s")
SELECT = re.compile(r"\(Select (TWO|THREE|FOUR)\.?\)", re.I)
SELECT_COUNT = {"TWO": 2, "THREE": 3, "FOUR": 4}


def clean(lines):
    text = textwrap.dedent("\n".join(lines)).strip("\n")
    return text.strip() and text.rstrip()


def split_items(block):
    lines = [l for l in block.splitlines() if not re.fullmatch(r"\s*=+\s*", l)]
    if any(NUMBERED.match(l) for l in lines):
        items, current = {}, None
        for line in lines:
            m = NUMBERED.match(line)
            if m:
                current = int(m.group(1))
                items[current] = [m.group(2)] if m.group(2) else []
            elif current is not None:
                items[current].append(line)
        return {k: clean(v) for k, v in items.items()}
    chunks = re.split(r"\n\s*\n", "\n".join(lines))
    return {i: clean(c.splitlines()) for i, c in enumerate((c for c in chunks if c.strip()), 1)}


def split_groups(text):
    """Split a file into groups of {'questions': str, 'answers': str, 'wrong answers': str}."""
    groups, current, section = [], None, None
    for line in text.splitlines():
        m = SECTION.match(line)
        if line.startswith("# ") or (m and m.group(1).lower() == "questions"):
            current, section = {}, None
            groups.append(current)
        if m:
            section = m.group(1).lower()
            current.setdefault(section, [])
        elif section and not line.startswith("# "):
            current[section].append(line)
    return [{k: "\n".join(v) for k, v in g.items()} for g in groups if "questions" in g]


def correct_choices(question, answer):
    content = [l for l in answer.splitlines() if l.strip() and not REFERENCE.match(l)]
    content = content[:1] + [l for l in content[1:] if not NOTE.match(l)]
    select = SELECT.search(question)
    if select:
        return [l.strip() for l in content[: SELECT_COUNT[select.group(1).upper()]]]
    joined = re.sub(r"\s+", " ", " ".join(content)).strip()
    return [joined] if joined else []


def parse_quiz(path):
    text = path.read_text(encoding="utf-8")
    heading = re.search(r"^#\s+(.+)$", text, re.M)
    title = re.sub(r"\s*--->.*$", "", heading.group(1)).strip().rstrip(":") if heading else path.stem
    questions = []
    for group in split_groups(text):
        qs = split_items(group["questions"])
        answers = split_items(group.get("answers", ""))
        wrongs = split_items(group.get("wrong answers", ""))
        for key, q in qs.items():
            if not q:
                continue
            answer = answers.get(key) or ""
            correct = correct_choices(q, answer)
            wrong = [l.strip() for l in (wrongs.get(key) or "").splitlines() if l.strip()]
            questions.append({
                "id": hashlib.sha1(q.encode()).hexdigest()[:10],
                "number": key,
                "question": q,
                "answer": answer or "(no answer provided)",
                "correct": correct,
                "wrong": wrong if correct else [],
            })
    return title, questions


def quiz_path(name):
    path = (QUIZ_DIR / name).resolve()
    in_set = path.parent == QUIZ_DIR or path.parent.parent == QUIZ_DIR
    if in_set and path.suffix == ".md" and path.is_file():
        return path
    return None


def list_sets():
    folders = [QUIZ_DIR] + sorted(p for p in QUIZ_DIR.iterdir() if p.is_dir() and not p.name.startswith("."))
    sets = []
    for folder in folders:
        quizzes = []
        for p in sorted(folder.glob("*.md")):
            title, qs = parse_quiz(p)
            quizzes.append({"name": p.relative_to(QUIZ_DIR).as_posix(), "title": title, "count": len(qs)})
        if folder != QUIZ_DIR or quizzes:
            label = "Other quizzes" if folder == QUIZ_DIR else folder.name.replace("_", " ").replace("-", " ").title()
            sets.append({"set": folder.relative_to(QUIZ_DIR).as_posix(), "title": label, "quizzes": quizzes})
    return sets


def metrics_path(quiz_name):
    path = (METRICS_DIR / quiz_name).with_suffix(".jsonl").resolve()
    if path.parent == METRICS_DIR or path.parent.parent == METRICS_DIR:
        return path
    return None


def load_attempts(path):
    attempts = []
    if path and path.is_file():
        for line in path.read_text(encoding="utf-8").splitlines():
            try:
                attempts.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return attempts


def save_attempt(data):
    path = quiz_path(str(data.get("quiz", "")))
    if not path:
        return None
    title, questions = parse_quiz(path)
    known = {q["id"]: q for q in questions}
    results = []
    for r in data.get("questions", []):
        q = known.get(str(r.get("id")))
        if q:
            results.append({
                "id": q["id"],
                "number": q["number"],
                "question": q["question"].split("\n")[0][:150],
                "correct": bool(r.get("correct")),
                "chosen": [str(c) for c in r.get("chosen") or []][:6],
            })
    if not results:
        return None
    score = sum(r["correct"] for r in results)
    name = path.relative_to(QUIZ_DIR).as_posix()
    record = {
        "timestamp": datetime.now().astimezone().isoformat(timespec="seconds"),
        "quiz": name,
        "title": title,
        "mode": "retry" if data.get("mode") == "retry" else "full",
        "shuffled": bool(data.get("shuffled")),
        "duration_sec": max(0, int(data.get("duration_sec") or 0)),
        "score": score,
        "total": len(results),
        "percent": round(100 * score / len(results)),
        "questions": results,
    }
    out = metrics_path(name)
    with METRICS_LOCK:
        out.parent.mkdir(parents=True, exist_ok=True)
        with out.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
    return record


def summarize(attempts):
    full = [a for a in attempts if a.get("mode") == "full"]
    return {
        "attempts": len(full),
        "retries": len(attempts) - len(full),
        "best": max((a["percent"] for a in full), default=None),
        "last": full[-1]["percent"] if full else None,
        "average": round(sum(a["percent"] for a in full) / len(full)) if full else None,
        "last_taken": attempts[-1]["timestamp"] if attempts else None,
        "title": attempts[-1].get("title") if attempts else None,
    }


def all_stats():
    stats = {}
    if METRICS_DIR.is_dir():
        for p in sorted(METRICS_DIR.rglob("*.jsonl")):
            attempts = load_attempts(p)
            if attempts:
                stats[p.relative_to(METRICS_DIR).with_suffix(".md").as_posix()] = summarize(attempts)
    return stats


def quiz_stats(name):
    attempts = load_attempts(metrics_path(name))
    by_question = {}
    for a in attempts:
        for r in a.get("questions", []):
            q = by_question.setdefault(r["id"], {
                "id": r["id"], "number": r.get("number"), "question": r.get("question", ""),
                "seen": 0, "missed": 0,
            })
            q["seen"] += 1
            q["missed"] += not r.get("correct")
            q["last_correct"] = bool(r.get("correct"))
    missed = sorted((q for q in by_question.values() if q["missed"]),
                    key=lambda q: (-q["missed"] / q["seen"], -q["missed"]))
    history = [{k: a.get(k) for k in ("timestamp", "mode", "score", "total", "percent", "duration_sec")}
               for a in reversed(attempts)]
    return {"summary": summarize(attempts), "history": history, "missed": missed}


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def send_json(self, data, status=200):
        body = json.dumps(data).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        url = urlparse(self.path)
        if url.path == "/api/quizzes":
            return self.send_json(list_sets())
        if url.path == "/api/stats":
            name = parse_qs(url.query).get("name", [""])[0]
            if not name:
                return self.send_json(all_stats())
            if not metrics_path(name) or not name.endswith(".md"):
                return self.send_json({"error": "invalid quiz name"}, 400)
            return self.send_json(quiz_stats(name))
        if url.path == "/api/quiz":
            path = quiz_path(parse_qs(url.query).get("name", [""])[0])
            if not path:
                return self.send_json({"error": "quiz not found"}, 404)
            title, qs = parse_quiz(path)
            return self.send_json({"title": title, "questions": qs})
        return super().do_GET()

    def do_POST(self):
        if urlparse(self.path).path != "/api/attempt":
            return self.send_json({"error": "not found"}, 404)
        length = int(self.headers.get("Content-Length") or 0)
        if not 0 < length <= 1_000_000:
            return self.send_json({"error": "bad request"}, 400)
        try:
            data = json.loads(self.rfile.read(length))
        except json.JSONDecodeError:
            return self.send_json({"error": "invalid JSON"}, 400)
        record = save_attempt(data) if isinstance(data, dict) else None
        if not record:
            return self.send_json({"error": "could not save attempt"}, 400)
        return self.send_json({"saved": metrics_path(record["quiz"]).relative_to(ROOT).as_posix(),
                               "percent": record["percent"]})

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    QUIZ_DIR.mkdir(exist_ok=True)
    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    url = f"http://localhost:{PORT}"
    print(f"Quiz app running at {url}  (Ctrl+C to stop)")
    threading.Timer(0.5, webbrowser.open, [url]).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nBye!")

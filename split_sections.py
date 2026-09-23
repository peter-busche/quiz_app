import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
args = [a for a in sys.argv[1:] if a != "--force"]
force = "--force" in sys.argv
src = ROOT / (args[0] if args else "questions_answers.md")
out = ROOT / "quizzes" / "udemy_questions"
out.mkdir(parents=True, exist_ok=True)

sections = []
for line in src.read_text(encoding="utf-8").splitlines(keepends=True):
    if line.startswith("# "):
        sections.append([line])
    elif sections:
        sections[-1].append(line)

for lines in sections:
    title = re.sub(r"\s*--->.*$", "", lines[0][2:]).strip().rstrip(":")
    m = re.match(r"Section\s+(\d+):\s*(.*)", title)
    num, name = (m.group(1).zfill(2), m.group(2)) if m else ("99", title)
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    path = out / f"{num}-{slug}.md"
    if path.exists() and not force:
        print(f"skip {path.relative_to(ROOT)} (exists; use --force to overwrite)")
        continue
    path.write_text("".join(lines).rstrip() + "\n", encoding="utf-8")
    print(path.relative_to(ROOT))

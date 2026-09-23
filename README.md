# Study Quiz

A simple local quiz app for studying. Load questions from markdown files, take multiple-choice quizzes, and track your performance.

## Quick Start

```bash
python3 quiz.py
```

Your browser opens at `http://localhost:8000`. The app serves itself—no dependencies, pure Python and vanilla JavaScript.

## How to Use

1. **Add quizzes:** Drop `.md` files into `quizzes/` or its subfolders (e.g., `quizzes/udemy_questions/`).
2. **Pick a quiz:** The home screen lists all your quiz sets. Click one to start.
3. **Answer questions:** For each question, select an option (or pick from multiple correct answers). Click **Next** to move on.
4. **See your score:** At the end, mark questions as "Got it" or "Missed it" if they were flashcards (no multiple choice).
5. **Track progress:** Click **View stats** on the home screen to see your best and last scores, and which questions you miss most.

## Quiz File Format

Each `.md` file is one quiz. Use this structure:

```markdown
# Your Quiz Title

### Questions:
- 1. 
First question text here

- 2. 
Second question text here

### Answers:
- 1. 
Correct answer for question 1
[Link to reference](https://example.com)

- 2. 
Correct answer for question 2

### Wrong Answers:
- 1. 
Wrong option A
Wrong option B
Wrong option C

- 2. 
Wrong option A
Wrong option B
Wrong option C
```

**Notes:**
- Question and answer numbers must match.
- Skip empty question numbers.
- For "Select TWO" questions, list 2 correct answers (one per line) and 3 wrong answers. The app shows all 5 as options.
- Reference links are ignored in answers. Same goes for lines starting with `-` (notes).
- Questions with no `### Wrong Answers` section work as flashcards: reveal and self-grade.

## Folder Structure

```
project14-quiz_app/
├── quiz.py              # Server
├── index.html           # UI (pure JavaScript)
├── split_sections.py    # One-time script to split a big .md into per-section files
├── quizzes/
│   ├── udemy_questions/
│   │   ├── 04-iam-aws-cli.md
│   │   └── ...
│   └── combined_sections/   # Add your own folders here
└── metrics/             # Auto-created; stores your attempt history as JSONL
    └── udemy_questions/
        └── 04-iam-aws-cli.jsonl
```

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `1–9` | Select an option |
| `Enter` | Submit (multi-select) or next question |
| `Space` | Reveal answer (flashcard mode) |
| `→` or `1` | Got it (flashcard mode) |
| `←` or `2` | Missed it (flashcard mode) |

## Features

- **Multiple choice** with automatic grading.
- **Shuffle** questions within a quiz (toggle on home screen; remembered).
- **Retry missed** only the questions you got wrong.
- **Local metrics:** Each quiz records your attempts to `metrics/<set>/<quiz>.jsonl`. One JSON object per line.
- **Stats:** Best score, last score, average, attempt history, and most-missed questions per quiz.
- **No backend:** Everything runs locally. No login, no accounts, no tracking.

## Metrics

Finished quiz attempts are saved as `.jsonl` files (one JSON per line) in `metrics/`. Each record includes:
- Timestamp and quiz name
- Mode (full run or retry)
- Score, percentage, and time taken
- Per-question results (id, number, your choice)

Use these files to analyze your progress outside the app, or delete them to reset your stats.

---

Made for AWS Certified Developer exam study.

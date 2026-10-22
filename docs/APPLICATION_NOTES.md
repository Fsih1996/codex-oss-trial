# Application notes (drafts)

Draft answers for short form fields, about 500 characters each. They describe **this repository only**.

Edit every draft so it sounds like you before you paste it. The facts below are what this repo can support. Do not add stars, downloads, users, production traffic, or a community that is not real.

Counts are `len(paragraph)` in Python, including spaces. If the form counts a different way, recount before submitting.

## Facts you can cite

- Name: `codex-oss-trial`
- What it is: a local Python todo command-line tool, plus a one-file greeting script (`hello.py`)
- Python: 3.11 or newer. Running the CLI needs no third-party packages
- Storage: a JSON file, `todo.json` by default, or `--file PATH`
- Commands: `add`, `list`, `done`, `remove`
- Tests: `pytest`, in `tests/`
- CI: GitHub Actions (`.github/workflows/ci.yml`) on Python 3.11 and 3.12
- License: MIT (`LICENSE`)
- Version `0.1.0` in `pyproject.toml` is a local label. This project is not published to PyPI
- Data stays on the machine where you run the command. No accounts and no network calls
- Task numbers start at 1 and change when a task is removed. There are no stable ids
- Maintainer: the GitHub account that owns the repo

## Project summary

471 characters.

codex-oss-trial is a local Python command-line todo list kept as a learning project. Tasks are stored in a JSON file you choose (todo.json by default). Commands are add, list, done, and remove. It is not deployed, not published on PyPI, and has no audience I can count, so this draft lists no users, stars, or downloads. A reviewer can check the command functions, the pytest tests for normal use and bad input, and GitHub Actions running those tests. The license is MIT.

## Why open source it

482 characters.

I published this CLI so a reviewer can clone it, run pytest, and read the commit history. That is the reason it is public. It is a personal learning repo: one maintainer, no user base, and no adoption story. Open source here means the behavior is written down. The README covers the commands and the local JSON file, CONTRIBUTING.md covers small pull requests, and SECURITY.md states that the tool has no network access and no accounts. Feedback on the code and the docs is welcome.

## What I learned

471 characters.

This repo is my practice loop for a small Python tool. I used argparse for add, list, done, and remove, stored tasks as JSON, and aimed tests at a temporary file so they never write a real todo.json. Unknown task numbers, empty titles, and a corrupt file exit with a short error instead of a traceback. GitHub Actions runs pytest on each push and pull request. The README states the status in plain words: a learning demo, with no claimed users and no production install.

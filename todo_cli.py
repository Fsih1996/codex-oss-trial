"""A tiny command-line todo list. Tasks are saved in a JSON file.

Usage:
    python todo_cli.py add "buy milk"
    python todo_cli.py list
    python todo_cli.py done 1
    python todo_cli.py remove 1
    python todo_cli.py --file /tmp/tasks.json list
"""

from __future__ import annotations

import argparse
import json
import os
import tempfile
from typing import TypedDict

DEFAULT_PATH = "todo.json"
MAX_TITLE_LENGTH = 200


class Task(TypedDict):
    title: str
    done: bool


def load_tasks(path: str = DEFAULT_PATH) -> list[Task]:
    """Return tasks from ``path``. A missing file is an empty list."""
    if not os.path.exists(path):
        return []
    try:
        with open(path, encoding="utf-8") as handle:
            data = json.load(handle)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Could not read tasks from {path}: invalid JSON") from exc
    if not isinstance(data, list):
        raise ValueError(f"Could not read tasks from {path}: expected a JSON list")

    tasks: list[Task] = []
    for index, item in enumerate(data, start=1):
        if (
            not isinstance(item, dict)
            or not isinstance(item.get("title"), str)
            or not isinstance(item.get("done"), bool)
        ):
            raise ValueError(
                f"Could not read tasks from {path}: "
                f"task {index} must have a string title and a boolean done"
            )
        tasks.append({"title": item["title"], "done": item["done"]})
    return tasks


def save_tasks(tasks: list[Task], path: str = DEFAULT_PATH) -> None:
    """Write ``tasks`` to ``path`` by replacing the file from a temp file."""
    directory = os.path.dirname(os.path.abspath(path))
    fd, tmp_path = tempfile.mkstemp(prefix=".todo-", suffix=".tmp", dir=directory)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(tasks, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        os.replace(tmp_path, path)
    except Exception:
        try:
            os.remove(tmp_path)
        except OSError:
            pass
        raise


def clean_title(title: str) -> str:
    """Return a stripped title, or raise ValueError if it cannot be stored."""
    cleaned = title.strip()
    if not cleaned:
        raise ValueError("Task title cannot be empty")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("Task title cannot contain line breaks")
    if len(cleaned) > MAX_TITLE_LENGTH:
        raise ValueError(
            f"Task title cannot be longer than {MAX_TITLE_LENGTH} characters"
        )
    return cleaned


def add_task(title: str, path: str = DEFAULT_PATH) -> int:
    """Append a task and return its 1-based number."""
    tasks = load_tasks(path)
    tasks.append({"title": clean_title(title), "done": False})
    save_tasks(tasks, path)
    return len(tasks)


def mark_done(number: int, path: str = DEFAULT_PATH) -> Task:
    """Mark task ``number`` done and return it."""
    tasks = load_tasks(path)
    if not 1 <= number <= len(tasks):
        raise IndexError(f"No task number {number}")
    tasks[number - 1]["done"] = True
    save_tasks(tasks, path)
    return tasks[number - 1]


def remove_task(number: int, path: str = DEFAULT_PATH) -> Task:
    """Delete task ``number`` and return it. Later numbers shift down."""
    tasks = load_tasks(path)
    if not 1 <= number <= len(tasks):
        raise IndexError(f"No task number {number}")
    removed = tasks.pop(number - 1)
    save_tasks(tasks, path)
    return removed


def format_task(number: int, task: Task) -> str:
    mark = "x" if task["done"] else " "
    return f"{number}. [{mark}] {task['title']}"


def build_parser(prog: str | None = None) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog=prog,
        description=(
            "Local todo list stored in a JSON file. "
            "A learning project: tasks stay on this machine."
        ),
        epilog=(
            "examples:\n"
            '  python todo_cli.py add "buy milk"\n'
            "  python todo_cli.py list\n"
            "  python todo_cli.py done 1\n"
            "  python todo_cli.py remove 1\n"
            "  python todo_cli.py --file /tmp/tasks.json list\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "-f",
        "--file",
        default=DEFAULT_PATH,
        metavar="PATH",
        help="JSON file that stores tasks (default: %(default)s)",
    )
    sub = parser.add_subparsers(dest="command", required=True, metavar="command")

    add = sub.add_parser("add", help="add a task")
    add.add_argument(
        "title",
        help=f"task text (one line, up to {MAX_TITLE_LENGTH} characters)",
    )

    sub.add_parser("list", help="show tasks in file order")

    done = sub.add_parser("done", help="mark a task done")
    done.add_argument("number", type=int, help="task number from list (starts at 1)")

    remove = sub.add_parser("remove", help="delete a task")
    remove.add_argument(
        "number", type=int, help="task number from list (starts at 1)"
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    # Keep help text stable when tests pass argv. A real process uses sys.argv[0],
    # so `python todo_cli.py` and the `codex-todo` entry point each name themselves.
    parser = build_parser(prog="todo_cli.py" if argv is not None else None)
    args = parser.parse_args(argv)
    path: str = args.file
    try:
        if args.command == "add":
            title = clean_title(args.title)
            number = add_task(title, path)
            print(f"Added task {number}: {title}")
        elif args.command == "list":
            tasks = load_tasks(path)
            if not tasks:
                print("No tasks yet.")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(format_task(number, task))
        elif args.command == "done":
            task = mark_done(args.number, path)
            print(f"Marked task {args.number} done: {task['title']}")
        elif args.command == "remove":
            task = remove_task(args.number, path)
            print(f"Removed task {args.number}: {task['title']}")
    except (IndexError, ValueError, OSError) as exc:
        parser.exit(1, f"Error: {exc}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

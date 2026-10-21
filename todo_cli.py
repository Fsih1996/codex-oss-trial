"""A tiny command-line todo list. Tasks are saved in todo.json.

Usage:
    python todo_cli.py add "buy milk"
    python todo_cli.py list
    python todo_cli.py done 1
    python todo_cli.py remove 1
"""
import argparse
import json
import os

DEFAULT_PATH = "todo.json"


def load_tasks(path=DEFAULT_PATH):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks, path=DEFAULT_PATH):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def add_task(title, path=DEFAULT_PATH):
    tasks = load_tasks(path)
    tasks.append({"title": title, "done": False})
    save_tasks(tasks, path)
    return len(tasks)  # the new task's number (starts at 1)


def mark_done(number, path=DEFAULT_PATH):
    tasks = load_tasks(path)
    if not 1 <= number <= len(tasks):
        raise IndexError(f"No task number {number}")
    tasks[number - 1]["done"] = True
    save_tasks(tasks, path)


def remove_task(number, path=DEFAULT_PATH):
    tasks = load_tasks(path)
    if not 1 <= number <= len(tasks):
        raise IndexError(f"No task number {number}")
    removed = tasks.pop(number - 1)
    save_tasks(tasks, path)
    return removed


def main(argv=None):
    parser = argparse.ArgumentParser(description="Simple todo list")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("add", help="add a task").add_argument("title")
    sub.add_parser("list", help="show all tasks")
    sub.add_parser("done", help="mark a task as done").add_argument("number", type=int)
    sub.add_parser("remove", help="delete a task").add_argument("number", type=int)
    args = parser.parse_args(argv)

    try:
        if args.command == "add":
            print(f"Added task {add_task(args.title)}")
        elif args.command == "list":
            for i, t in enumerate(load_tasks(), start=1):
                print(f"{i}. [{'x' if t['done'] else ' '}] {t['title']}")
        elif args.command == "done":
            mark_done(args.number)
        elif args.command == "remove":
            remove_task(args.number)
    except IndexError as e:
        parser.exit(1, f"Error: {e}\n")


if __name__ == "__main__":
    main()

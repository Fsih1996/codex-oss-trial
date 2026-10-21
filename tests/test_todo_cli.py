import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import todo_cli  # noqa: E402


@pytest.fixture
def path(tmp_path):
    return str(tmp_path / "todo.json")


def test_add_task(path):
    assert todo_cli.add_task("buy milk", path) == 1
    assert todo_cli.load_tasks(path) == [{"title": "buy milk", "done": False}]


def test_mark_done(path):
    todo_cli.add_task("a", path)
    todo_cli.mark_done(1, path)
    assert todo_cli.load_tasks(path)[0]["done"] is True


def test_remove_task(path):
    todo_cli.add_task("a", path)
    todo_cli.add_task("b", path)
    removed = todo_cli.remove_task(1, path)
    assert removed["title"] == "a"
    assert [t["title"] for t in todo_cli.load_tasks(path)] == ["b"]


def test_bad_number(path):
    with pytest.raises(IndexError):
        todo_cli.mark_done(5, path)

from pathlib import Path

import pytest

import todo_cli


@pytest.fixture
def path(tmp_path):
    return str(tmp_path / "todo.json")


def test_add_task(path):
    assert todo_cli.add_task("buy milk", path) == 1
    assert todo_cli.load_tasks(path) == [{"title": "buy milk", "done": False}]


def test_add_strips_title_and_keeps_unicode(path):
    assert todo_cli.add_task("  买牛奶  ", path) == 1
    stored = Path(path).read_text(encoding="utf-8")
    assert "买牛奶" in stored
    assert "\\u" not in stored
    assert todo_cli.load_tasks(path) == [{"title": "买牛奶", "done": False}]


def test_mark_done(path):
    todo_cli.add_task("a", path)
    task = todo_cli.mark_done(1, path)
    assert task == {"title": "a", "done": True}
    assert todo_cli.load_tasks(path)[0]["done"] is True


def test_remove_task(path):
    todo_cli.add_task("a", path)
    todo_cli.add_task("b", path)
    removed = todo_cli.remove_task(1, path)
    assert removed["title"] == "a"
    assert [task["title"] for task in todo_cli.load_tasks(path)] == ["b"]


def test_bad_number(path):
    with pytest.raises(IndexError, match="No task number 5"):
        todo_cli.mark_done(5, path)


def test_missing_file_is_empty_list(path):
    assert todo_cli.load_tasks(path) == []


def test_files_stay_independent(tmp_path):
    first = str(tmp_path / "a.json")
    second = str(tmp_path / "b.json")
    todo_cli.add_task("only-a", first)
    assert todo_cli.load_tasks(second) == []
    assert todo_cli.load_tasks(first)[0]["title"] == "only-a"


def test_empty_and_newline_titles_are_rejected(path):
    for title in ("", "   ", "milk\nbread"):
        with pytest.raises(ValueError):
            todo_cli.add_task(title, path)
    assert todo_cli.load_tasks(path) == []


def test_title_length_limit(path):
    todo_cli.add_task("a" * todo_cli.MAX_TITLE_LENGTH, path)
    with pytest.raises(ValueError, match="200"):
        todo_cli.add_task("b" * (todo_cli.MAX_TITLE_LENGTH + 1), path)
    assert len(todo_cli.load_tasks(path)) == 1


def test_corrupt_json(path):
    Path(path).write_text("{", encoding="utf-8")
    with pytest.raises(ValueError, match="invalid JSON"):
        todo_cli.load_tasks(path)


def test_json_with_the_wrong_shape(path):
    Path(path).write_text('{"title": "nope"}', encoding="utf-8")
    with pytest.raises(ValueError, match="JSON list"):
        todo_cli.load_tasks(path)

    Path(path).write_text('[{"title": "a"}]', encoding="utf-8")
    with pytest.raises(ValueError, match="task 1"):
        todo_cli.load_tasks(path)


def test_save_leaves_no_temp_file(path):
    todo_cli.add_task("a", path)
    directory = Path(path).parent
    leftovers = list(directory.glob(".todo-*.tmp"))
    assert leftovers == []
    assert Path(path).is_file()


def test_cli_round_trip(path, capsys):
    assert todo_cli.main(["--file", path, "add", "  buy milk  "]) == 0
    assert todo_cli.main(["--file", path, "list"]) == 0
    assert todo_cli.main(["--file", path, "done", "1"]) == 0
    assert todo_cli.main(["--file", path, "list"]) == 0
    assert todo_cli.main(["--file", path, "remove", "1"]) == 0
    assert todo_cli.main(["--file", path, "list"]) == 0

    out = capsys.readouterr().out
    assert "Added task 1: buy milk" in out
    assert "1. [ ] buy milk" in out
    assert "Marked task 1 done: buy milk" in out
    assert "1. [x] buy milk" in out
    assert "Removed task 1: buy milk" in out
    assert out.strip().endswith("No tasks yet.")
    assert todo_cli.load_tasks(path) == []


def test_cli_empty_list(path, capsys):
    assert todo_cli.main(["-f", path, "list"]) == 0
    assert capsys.readouterr().out.strip() == "No tasks yet."


def test_cli_unknown_number_exits(path, capsys):
    with pytest.raises(SystemExit) as caught:
        todo_cli.main(["--file", path, "done", "3"])
    assert caught.value.code == 1
    assert "No task number 3" in capsys.readouterr().err


def test_cli_rejects_empty_title(path, capsys):
    with pytest.raises(SystemExit) as caught:
        todo_cli.main(["--file", path, "add", "  "])
    assert caught.value.code == 1
    assert "cannot be empty" in capsys.readouterr().err
    assert not Path(path).exists()


def test_add_requires_a_title():
    with pytest.raises(SystemExit) as caught:
        todo_cli.main(["add"])
    assert caught.value.code == 2


def test_help_lists_examples(capsys):
    with pytest.raises(SystemExit) as caught:
        todo_cli.main(["--help"])
    assert caught.value.code == 0
    help_text = capsys.readouterr().out
    assert "buy milk" in help_text
    assert "--file" in help_text
    assert "learning project" in help_text

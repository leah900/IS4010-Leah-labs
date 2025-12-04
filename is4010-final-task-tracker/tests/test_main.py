from pathlib import Path
import json
import tempfile
from src.main import load_tasks, save_tasks, add_task, list_tasks, init_store, complete_task, delete_task


def test_load_save_roundtrip(tmp_path, capsys):
    p = tmp_path / "tasks.json"
    assert load_tasks(p) == []
    save_tasks(p, [{"id": 1, "description": "x", "done": False}])
    assert load_tasks(p)[0]["description"] == "x"


def test_add_and_list(tmp_path, capsys):
    p = tmp_path / "tasks.json"
    add_task(p, "Test task")
    # capture output from list
    list_tasks(p)
    captured = capsys.readouterr()
    assert "Test task" in captured.out


def test_complete_and_delete(tmp_path, capsys):
    p = tmp_path / "tasks.json"
    add_task(p, "A")
    add_task(p, "B")
    complete_task(p, 1)
    tasks = load_tasks(p)
    assert tasks[0]["done"] is True
    delete_task(p, 1)
    tasks2 = load_tasks(p)
    assert all(t["id"] != 1 for t in tasks2)

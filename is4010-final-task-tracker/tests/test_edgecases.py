from pathlib import Path
import json
import pytest
from src.main import load_tasks, save_tasks, add_task


def test_missing_store_returns_empty(tmp_path):
    p = tmp_path / "nope.json"
    assert load_tasks(p) == []


def test_corrupted_json_handled(tmp_path, capsys):
    p = tmp_path / "bad.json"
    p.write_text("not json")
    assert load_tasks(p) == []


def test_duplicate_descriptions_allowed(tmp_path):
    p = tmp_path / "tasks.json"
    add_task(p, "Same")
    add_task(p, "Same")
    tasks = load_tasks(p)
    assert len([t for t in tasks if t["description"] == "Same"]) == 2


def test_long_description(tmp_path, capsys):
    p = tmp_path / "tasks.json"
    long = "x" * 5000
    add_task(p, long)
    tasks = load_tasks(p)
    assert tasks[0]["description"] == long

import json
import argparse
from pathlib import Path
from typing import List, Dict


def load_tasks(path: Path) -> List[Dict]:
    if not path.exists():
        return []
    try:
        return json.loads(path.read_text())
    except Exception:
        return []


def save_tasks(path: Path, tasks: List[Dict]):
    path.write_text(json.dumps(tasks, indent=2))


def add_task(path: Path, description: str):
    tasks = load_tasks(path)
    task_id = max((t.get("id", 0) for t in tasks), default=0) + 1
    tasks.append({"id": task_id, "description": description, "done": False})
    save_tasks(path, tasks)
    print(f"Added task {task_id}: {description}")
import json
import argparse
from pathlib import Path
from typing import List, Dict


def load_tasks(path: Path) -> List[Dict]:
    if not path.exists():
        return []
    try:
        return json.loads(path.read_text())
    except Exception:
        return []


def save_tasks(path: Path, tasks: List[Dict]):
    path.write_text(json.dumps(tasks, indent=2))


def add_task(path: Path, description: str):
    tasks = load_tasks(path)
    task_id = max((t.get("id", 0) for t in tasks), default=0) + 1
    tasks.append({"id": task_id, "description": description, "done": False})
    save_tasks(path, tasks)
    print(f"Added task {task_id}: {description}")


def list_tasks(path: Path):
    tasks = load_tasks(path)
    if not tasks:
        print("No tasks.")
        return
    for t in tasks:
        status = "✓" if t.get("done") else " "
        print(f"[{status}] {t.get('id')}: {t.get('description')}")


def complete_task(path: Path, task_id: int):
    tasks = load_tasks(path)
    for t in tasks:
        if t.get("id") == task_id:
            t["done"] = True
            save_tasks(path, tasks)
            print(f"Marked {task_id} complete")
            return
    print(f"Task {task_id} not found")


def delete_task(path: Path, task_id: int):
    tasks = load_tasks(path)
    new = [t for t in tasks if t.get("id") != task_id]
    if len(new) == len(tasks):
        print(f"Task {task_id} not found")
        return
    save_tasks(path, new)
    print(f"Deleted {task_id}")


def init_store(path: Path):
    if path.exists():
        print("Store already exists")
        return
    save_tasks(path, [])
    print(f"Initialized {path}")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    sub = parser.add_subparsers(dest="command")

    init = sub.add_parser("init")
    init.add_argument("path")

    add = sub.add_parser("add")
    add.add_argument("path")
    add.add_argument("description")

    list_p = sub.add_parser("list")
    list_p.add_argument("path")

    complete = sub.add_parser("complete")
    complete.add_argument("path")
    complete.add_argument("id", type=int)

    delete = sub.add_parser("delete")
    delete.add_argument("path")
    delete.add_argument("id", type=int)

    args = parser.parse_args(argv)
    path = Path(args.path)

    if args.command == "init":
        init_store(path)
    elif args.command == "add":
        add_task(path, args.description)
    elif args.command == "list":
        list_tasks(path)
    elif args.command == "complete":
        complete_task(path, args.id)
    elif args.command == "delete":
        delete_task(path, args.id)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

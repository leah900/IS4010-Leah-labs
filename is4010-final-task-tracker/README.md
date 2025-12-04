# is4010-final-task-tracker

Simple Task Tracker CLI for IS4010 — add/list/complete/delete tasks stored in a local JSON file.

![Tests](https://github.com/leah900/IS4010-Leah-labs/actions/workflows/is4010-final-task-tracker-tests.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)

## Quickstart

```bash
python -m src.main init tasks.json
python -m src.main add tasks.json "Buy milk"
python -m src.main list tasks.json
```

Advanced examples:

```bash
python -m src.main add tasks.json "Write report"
python -m src.main complete tasks.json 2
python -m src.main delete tasks.json 1
```

## Features

- Add tasks
- List tasks
- Mark tasks complete
- Delete tasks

## Testing

Run:

```bash
pytest
```

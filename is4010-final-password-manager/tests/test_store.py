import tempfile
import os
import pytest
from is4010_final_password_manager import store


def test_init_and_load():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        path = tmp.name
    try:
        store.init_store(path, 'pass123')
        data = store.load_store(path, 'pass123')
        assert 'entries' in data
    finally:
        os.remove(path)


def test_add_and_get():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        path = tmp.name
    try:
        store.init_store(path, 'pwd')
        store.add_entry(path, 'pwd', 'github', 'me', 's3cret')
        e = store.get_entry(path, 'pwd', 'github')
        assert e is not None
        assert e['username'] == 'me'
    finally:
        os.remove(path)


def test_list_entries_empty():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        path = tmp.name
    try:
        store.init_store(path, 'x')
        names = store.list_entries(path, 'x')
        assert names == []
    finally:
        os.remove(path)

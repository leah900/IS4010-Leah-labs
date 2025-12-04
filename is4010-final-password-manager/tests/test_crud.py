import tempfile
import os
from is4010_final_password_manager import store


def test_update_and_delete_and_search():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        path = tmp.name
    try:
        store.init_store(path, 'master')
        store.add_entry(path, 'master', 'site1', 'alice', 'p1')
        store.add_entry(path, 'master', 'site2', 'bob', 'p2')
        # update
        ok = store.update_entry(path, 'master', 'site1', username='alice2')
        assert ok
        e = store.get_entry(path, 'master', 'site1')
        assert e['username'] == 'alice2'
        # search
        results = store.search_entries(path, 'master', 'ali')
        assert len(results) == 1
        # delete
        ok = store.delete_entry(path, 'master', 'site2')
        assert ok
        assert store.get_entry(path, 'master', 'site2') is None
    finally:
        os.remove(path)

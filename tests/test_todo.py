from pathlib import Path

from src.modules.todo import TodoStore


def test_add_toggle_delete(tmp_path: Path) -> None:
    path = tmp_path / "tasks.json"
    store = TodoStore(path)
    t1 = store.add("Test")
    assert path.exists()
    data = path.read_text()
    assert "Test" in data
    assert not t1.done

    store.toggle(t1.id)
    assert store.todos[0].done

    store.delete(t1.id)
    assert store.todos == []
    assert path.exists()
    assert path.read_text() == "[]"

from __future__ import annotations

import json
from pathlib import Path
from typing import List

from .model import Todo


class TodoStore:
    """Verwaltet die Liste der Todos und speichert automatisch."""

    def __init__(self, path: Path | None = None) -> None:
        self.path = path or Path.home() / ".experimental_agent_tasks.json"
        self.todos: List[Todo] = []
        self._load()

    # interne Hilfsmethoden
    def _load(self) -> None:
        if self.path.exists():
            with self.path.open("r", encoding="utf-8") as fh:
                data = json.load(fh)
            self.todos = [Todo(**item) for item in data]
        else:
            self.todos = []
            self._save()

    def _save(self) -> None:
        with self.path.open("w", encoding="utf-8") as fh:
            json.dump([t.dict() for t in self.todos], fh, indent=2, ensure_ascii=False)

    # API-Methoden
    def add(self, text: str) -> Todo:
        next_id = max([t.id for t in self.todos], default=0) + 1
        todo = Todo(id=next_id, text=text, done=False)
        self.todos.append(todo)
        self._save()
        return todo

    def toggle(self, todo_id: int) -> None:
        for t in self.todos:
            if t.id == todo_id:
                t.done = not t.done
                break
        self._save()

    def delete(self, todo_id: int) -> None:
        self.todos = [t for t in self.todos if t.id != todo_id]
        self._save()

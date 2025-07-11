"""Grafische Oberfläche für die Todo-Liste.

Dieser Code wird nicht automatisch getestet.
"""  # pragma: no cover
from __future__ import annotations

from tkinter import END, Checkbutton, Entry, Frame, IntVar, Menu, Tk
from typing import Any

from .storage import TodoStore


class TodoGUI:
    """Einfache GUI zum Verwalten von Todos."""

    def __init__(self, store: TodoStore | None = None) -> None:
        self.store = store or TodoStore()
        self.root = Tk()
        self.root.title("Todos")

        self.frame = Frame(self.root)
        self.frame.pack(fill="both", expand=True)

        self.entry = Entry(self.root)
        self.entry.pack(fill="x")
        self.entry.bind("<Control-Return>", self.add_current)

        self.render_todos()

    def render_todos(self) -> None:
        for widget in self.frame.winfo_children():
            widget.destroy()
        for todo in self.store.todos:
            var = IntVar(value=1 if todo.done else 0)
            chk = Checkbutton(
                self.frame,
                text=todo.text,
                variable=var,
                command=lambda i=todo.id: self.toggle(i),  # type: ignore[misc]
            )
            chk.pack(anchor="w")
            chk.bind(
                "<Button-3>", lambda e, i=todo.id: self._show_menu(e, i)  # type: ignore[misc]
            )

    def add_current(self, event=None) -> None:  # noqa: ANN001
        text = self.entry.get().strip()
        if text:
            self.store.add(text)
            self.entry.delete(0, END)
            self.render_todos()

    def toggle(self, todo_id: int) -> None:
        self.store.toggle(todo_id)
        self.render_todos()

    def _show_menu(self, event: Any, todo_id: int) -> None:
        menu = Menu(self.root, tearoff=0)
        menu.add_command(label="Delete", command=lambda: self.delete(todo_id))
        menu.tk_popup(event.x_root, event.y_root)

    def delete(self, todo_id: int) -> None:
        self.store.delete(todo_id)
        self.render_todos()

    def run(self) -> None:
        self.root.mainloop()


def main() -> None:
    TodoGUI().run()


if __name__ == "__main__":
    main()

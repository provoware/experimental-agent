import tkinter as tk
from tkinter import simpledialog

import pyperclip

from .backend import TemplateManager


class TemplateGUI:
    """Simple GUI for managing text templates."""

    def __init__(self, manager: TemplateManager | None = None):
        self.manager = manager or TemplateManager()
        self.root = tk.Tk()
        self.root.title('Textvorlagen')
        tk.Button(
            self.root,
            text='Neu',
            command=self.add_template
        ).grid(row=0, column=0, pady=5)
        self.table_frame = tk.Frame(self.root)
        self.table_frame.grid(row=1, column=0, padx=10)
        self.refresh()

    def add_template(self) -> None:
        name = simpledialog.askstring(
            'Vorlage',
            'Name der Vorlage:',
            parent=self.root,
        )
        if not name:
            return
        content = simpledialog.askstring(
            'Vorlage',
            'Inhalt:',
            parent=self.root,
        )
        if content is None:
            return
        self.manager.add_or_update(name, content)
        self.refresh()

    def copy(self, name: str) -> None:
        text = self.manager.get(name)
        pyperclip.copy(text)

    def refresh(self) -> None:
        for widget in self.table_frame.winfo_children():
            widget.destroy()
        tk.Label(
            self.table_frame, text='Name', width=20, anchor='w'
        ).grid(row=0, column=0, padx=2, pady=2)
        tk.Label(
            self.table_frame, text='Inhalt', width=40, anchor='w'
        ).grid(row=0, column=1, padx=2, pady=2)
        tk.Label(self.table_frame, text='').grid(row=0, column=2)
        for idx, (name, content) in enumerate(
            self.manager.list_templates(), start=1
        ):
            tk.Label(
                self.table_frame, text=name, anchor='w'
            ).grid(row=idx, column=0, sticky='w')
            tk.Label(
                self.table_frame, text=content, anchor='w'
            ).grid(row=idx, column=1, sticky='w')
            tk.Button(
                self.table_frame,
                text='Kopieren',
                command=lambda n=name: self.copy(n),
            ).grid(row=idx, column=2, padx=5)

    def run(self) -> None:
        self.root.mainloop()


def main() -> None:
    TemplateGUI().run()


if __name__ == '__main__':
    main()

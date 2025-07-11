"""Einfache grafische Oberflaeche fuer den Controller."""

try:
    import tkinter as tk
except Exception:  # falls tkinter nicht vorhanden ist
    tk = None

import os
from main import Controller

def _list_modules():
    """Liest alle vorhandenen Moduldateien im Ordner ``src`` aus."""
    module_files = [f for f in os.listdir(os.path.dirname(__file__))
                    if f.endswith('.py') and f not in {'__init__.py', 'gui.py'}]
    return [os.path.splitext(f)[0] for f in module_files]

def gui_message():
    """Gibt eine kurze Statusmeldung zurueck."""
    return "GUI bereit"


def start_gui():
    """Erstellt das Hauptfenster mit Buttons."""
    if tk is None:
        raise RuntimeError("tkinter nicht verfuegbar")
    root = tk.Tk()
    root.title("Experimental Agent")

    controller = Controller()

    tk.Button(root, text="Controller starten",
              command=lambda: print(controller.run())).pack(pady=10)

    mod_frame = tk.LabelFrame(root, text="Module")
    mod_frame.pack(pady=5, fill="x")

    for mod in _list_modules():
        tk.Button(mod_frame, text=mod,
                  command=lambda m=mod: print(controller.add_module(m)))\
            .pack(fill="x")

    entry = tk.Entry(mod_frame)
    entry.pack(fill="x", pady=2)
    tk.Button(mod_frame, text="Neues Modul laden",
              command=lambda: print(controller.add_module(entry.get()))).pack(pady=2)

    tk.Button(root, text="Beenden", command=root.quit).pack(pady=10)
    return root


if __name__ == "__main__":
    app = start_gui()
    print(gui_message())
    app.mainloop()

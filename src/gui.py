"""Einfache grafische Oberflaeche fuer den Controller."""

try:
    import tkinter as tk
except Exception:  # falls tkinter nicht vorhanden ist
    tk = None

def gui_message():
    """Gibt eine kurze Statusmeldung zurueck."""
    return "GUI bereit"


def start_gui():
    """Erstellt das Hauptfenster mit Buttons."""
    if tk is None:
        raise RuntimeError("tkinter nicht verfuegbar")
    root = tk.Tk()
    root.title("Experimental Agent")
    tk.Button(root, text="Controller starten", command=lambda: print("Controller laeuft"))\
        .pack(pady=10)
    tk.Button(root, text="Beenden", command=root.quit).pack(pady=10)
    return root


if __name__ == "__main__":
    app = start_gui()
    print(gui_message())
    app.mainloop()

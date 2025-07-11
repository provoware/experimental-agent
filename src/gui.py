"""Einfache grafische Oberflaeche fuer den Controller."""

try:
    import tkinter as tk
except Exception:  # falls tkinter nicht vorhanden ist
    tk = None

def gui_message():
    """Gibt eine kurze Statusmeldung zurueck."""
    return "GUI bereit"


def start_gui():
    """Erstellt das Hauptfenster mit moderner Aufteilung."""
    if tk is None:
        raise RuntimeError("tkinter nicht verfuegbar")

    root = tk.Tk()
    root.title("Experimental Agent")

    # Header
    header = tk.Frame(root, bg="#2c3e50", height=50)
    header.pack(side="top", fill="x")
    tk.Label(
        header,
        text="Experimental Agent Dashboard",
        fg="white",
        bg="#2c3e50",
        font=("Arial", 16, "bold"),
    ).pack(pady=10)

    # Hauptbereich mit Sidebar und Inhalt
    main = tk.Frame(root)
    main.pack(expand=True, fill="both")

    sidebar = tk.Frame(main, width=180, bg="#ecf0f1")
    sidebar.pack(side="left", fill="y")

    content = tk.Frame(main, bg="white")
    content.pack(side="left", expand=True, fill="both")

    status = tk.Label(content, text="", bg="white")
    status.pack(pady=20)

    def start_controller():
        status.config(text="Controller laeuft")

    tk.Button(sidebar, text="Controller starten", command=start_controller).pack(
        pady=10, padx=10, fill="x"
    )
    tk.Button(sidebar, text="Beenden", command=root.quit).pack(
        pady=10, padx=10, fill="x"
    )

    # Fusszeile in vier Teile
    footer = tk.Frame(root, bg="#bdc3c7")
    footer.pack(side="bottom", fill="x")
    for text in ["Abschnitt 1", "Abschnitt 2", "Abschnitt 3", "Abschnitt 4"]:
        tk.Label(footer, text=text, bg="#bdc3c7").pack(
            side="left", expand=True, fill="x", padx=5, pady=5
        )

    return root


if __name__ == "__main__":
    app = start_gui()
    print(gui_message())
    app.mainloop()

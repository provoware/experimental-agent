# Release erstellen

Diese Schritte erzeugen eine portierbare AppImage-Datei.

1. `pip install pyinstaller appimagetool` – installiert die Werkzeuge.
2. `pyinstaller --onefile src/main.py` – erzeugt ein einzelnes Programm.
3. `appimagetool dist/main` – baut daraus eine AppImage-Datei (AppImage = portable Linux-Anwendung).

Die fertige Datei findest du im Ordner `dist`. Sie kann auf anderen Linux-Systemen ohne weitere Installation gestartet werden.

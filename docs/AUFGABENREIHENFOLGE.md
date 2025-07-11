# Aufgabenreihenfolge

Diese Liste erklaert Schritt fuer Schritt, wie du das Projekt startest. Fachbegriffe stehen in Klammern und werden kurz erklaert.

1. `git clone <REPO-URL>` – klont das Projekt aus der Versionsverwaltung.
2. `cd experimental-agent` – wechselt in den frisch angelegten Ordner.
3. `python3 --version` – zeigt die installierte Python-Version. Wenn Python fehlt:
   `sudo apt update && sudo apt install python3 python3-venv python3-pip`
   (**apt** = Paketverwaltung von Debian/Ubuntu).
4. `python3 -m venv venv` – erstellt eine *virtuelle Umgebung* (geschuetzter Arbeitsbereich).
5. `source venv/bin/activate` – aktiviert diese Umgebung.
6. `pip install -r requirements.txt` – installiert benoetigte Pakete mit **pip** (Paketmanager fuer Python).
7. `pytest -q` – startet die automatischen Tests.
8. `python src/main.py` – laesst den Controller (Steuerprogramm) laufen.
9. Mit `deactivate` beendest du die virtuelle Umgebung. Danach kann sie bei Bedarf mit `rm -r venv` entfernt werden.

Weitere Nuetzliche Befehle:
- `pip list` zeigt alle installierten Pakete an.
- `pip install --upgrade pip` aktualisiert **pip**.
- `python3 -m venv --help` liefert Hilfe zur virtuellen Umgebung.

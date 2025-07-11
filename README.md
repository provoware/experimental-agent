# experimental-agent

Der **Controller** (Steuerprogramm) ist das Herzstück dieses Projekts. Er verwaltet alle Module und soll unveränderlich laufen.

## Installation

1. Terminal öffnen.
2. `git clone <REPO-URL>` (Repository aus der Versionsverwaltung klonen).
3. `cd experimental-agent` (in den Ordner wechseln).
4. `python3 --version` (Version kontrollieren). Falls nicht vorhanden: `sudo apt update && sudo apt install python3 python3-venv python3-pip` (**apt** ist die Paketverwaltung von Debian/Ubuntu).
5. `python3 -m venv venv` (virtuelle Umgebung *virtual environment* - isolierter Arbeitsbereich - anlegen).
6. `source venv/bin/activate` (Umgebung aktivieren).
7. `pip install -r requirements.txt` (**pip** ist der Paketmanager für Python, installiert hier die Abhängigkeiten).

## Anwendung

1. `pytest` (Tests ausführen und überprüfen).
2. `python src/main.py` (Controller starten).

## Was macht der Controller?

Der Controller sorgt dafür, dass alle Teile des Systems ordnungsgemäß laufen. Er erkennt Fehler und kann sie selbst beheben ("Selbstheilung").

## Weitere Tipps für Einsteiger

* Falls Python fehlt: `sudo apt install python3` (Installation über **apt** - Paketverwaltung für Debian/Ubuntu).
* Mit `pip list` lassen sich installierte Pakete anzeigen.
* `pip install --upgrade pip` aktualisiert **pip** auf die neueste Version.
* Um die virtuelle Umgebung zu verlassen, `deactivate` eingeben. Danach kann sie mit `rm -r venv` gelöscht werden.

### Weiterführende Tipps

* `git status` zeigt den aktuellen Stand der Dateien.
* `git add <datei>` fügt eine Datei zum nächsten Commit hinzu (Commit = gespeicherter Versionsschritt).
* `git commit -m "Nachricht"` speichert die Änderungen dauerhaft.
* `git push` überträgt den Commit auf den Server.

### Laien-Tipps

* `git pull` holt die neuesten Daten vom Server (Server = zentrale Ablage).
* `git branch neuer-zweig` erstellt einen neuen Branch (Branch = Entwicklungszweig).
* `git checkout neuer-zweig` wechselt auf den neuen Branch.
* `python beispiel.py` führt ein Python-Programm aus (Python = Programmiersprache).
* `pip uninstall paketname` entfernt ein Paket (Paket = Sammlung von Programmteilen).
Weitere ausführliche Hinweise findest du in `docs/LAIENTIPPS.md`.
Die Liste dort enthaelt jetzt auch Befehle wie `pwd`, `cat`, `nano`, `history`, `man`, `apt update`, `df -h`, `curl` und `wget`, jeweils kurz beschrieben.

Zusaetzlich gibt es eine kleine grafische Oberflaeche. Starte sie mit `python src/gui.py`.
Die Tippsdatei enthaelt jetzt auch Befehle wie `less`, `tail` oder `ssh`.

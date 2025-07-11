# experimental-agent

Dieses Projekt zeigt einen unveränderlichen zentralen Controller. Er lässt sich über eine einfache Oberfläche steuern.

## Schritt-für-Schritt-Anleitung

1. `git clone <REPO-URL>` – Quellcode vom Server holen.
2. `cd experimental-agent` – in den Projektordner wechseln.
3. `python -m venv venv` – virtuelle Umgebung (getrennter Arbeitsbereich) anlegen.
4. `source venv/bin/activate` – virtuelle Umgebung aktivieren.
5. `pytest` – Tests ausführen.
6. `python src/main.py` – Controller starten.

## Tipps für Einsteiger

- `git status` (zeigt den aktuellen Zustand der Dateien im Repository [Projektarchiv]).
- `git pull` (holt die neuesten Änderungen vom Server).
- `git help <Befehl>` (zeigt die Hilfeseite [Manual] zu einem git-Befehl).
- `git log` (listet die letzten Versionen [Commits] auf).
- `rm -rf .pytest_cache` (entfernt den Test-Zwischenspeicher [Cache], falls Fehler auftreten).
- `deactivate` (beendet die virtuelle Umgebung).

## Weiterführende Tipps

- `git branch` (listet alle Entwicklungszweige [Branches] auf).
- `git checkout -b <name>` (erstellt und wechselt in einen neuen Entwicklungszweig [Branch]).
- `python -m venv venv` (legt eine virtuelle Umgebung [isolierter Python-Arbeitsbereich] an).
- `source venv/bin/activate` (aktiviert die virtuelle Umgebung).
- `pip install -r requirements.txt` (installiert benötigte Pakete [Dependencies]).
- `git remote -v` (zeigt die eingerichteten entfernten Server [Remote-Repositories]).

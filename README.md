# experimental-agent

Dieses Projekt zeigt einen unveränderlichen zentralen Controller. Er lässt sich über eine einfache Oberfläche steuern.

## Befehle zum Starten

```bash
git clone <REPO-URL>    # Quellcode vom Server holen
cd experimental-agent   # in den Projektordner wechseln
pytest                  # Tests ausführen
python src/main.py      # Controller starten
```

## Tipps für Einsteiger

- `git status` (zeigt den aktuellen Zustand der Dateien im Repository [Projektarchiv]).
- `git pull` (holt die neuesten Änderungen vom Server).
- `rm -rf .pytest_cache` (entfernt den Test-Zwischenspeicher [Cache], falls Fehler auftreten).

## Weiterführende Tipps

- `git branch` (listet alle Entwicklungszweige [Branches] auf).
- `git checkout -b <name>` (erstellt und wechselt in einen neuen Entwicklungszweig [Branch]).
- `python -m venv venv` (legt eine virtuelle Umgebung [isolierter Python-Arbeitsbereich] an).
- `source venv/bin/activate` (aktiviert die virtuelle Umgebung).

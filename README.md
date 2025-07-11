# experimental-agent

Dieses Projekt zeigt einen unveränderlichen zentralen Controller. Er lässt sich über eine einfache Oberfläche steuern.

## Befehle zum Starten

1. `git clone <REPO-URL>` (holt den Quellcode vom Server)
2. `cd experimental-agent` (wechseln in den Projektordner)
3. `pytest` (startet die Tests)
4. `python src/main.py` (startet den Controller)
=======
3. `pytest` (startet die Tests, falls welche existieren)


## Weiterfuehrende Vorschlaege fuer Einsteiger

- **Werkzeuge installieren**: `python -m pip install flake8 pytest build` (installiert die benoetigten Tools).
- **Code-Analyse (lint)**: `flake8 .` prueft den Code auf typische Fehler.
- **Tests ausfuehren**: `pytest` startet die automatischen Tests.
- **Build** (Paket erzeugen): `python -m build` erstellt ein installierbares Paket.

Der neue CI-Workflow fuehrt diese Schritte automatisch aus.

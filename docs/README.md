# Dokumentation

Hier findest du zusätzliche Informationen zum Projekt.

## Controller erklärt

Der Controller (Steuerprogramm) verwaltet alle Module und prüft, ob sie korrekt laufen. Wenn ein Fehler auftaucht, versucht er ihn automatisch zu beheben.

## Installationshinweise

1. `git clone <REPO-URL>` – holt den Code.
2. `cd experimental-agent`
3. `python3 --version` (prüft die Version). Falls Python nicht vorhanden:
   `sudo apt update && sudo apt install python3 python3-venv python3-pip` (**apt** = Paketverwaltung).
4. `python3 -m venv venv` (legt eine virtuelle Umgebung an, ein geschützter Arbeitsbereich).
5. `source venv/bin/activate` (Umgebung aktivieren).
6. `pip install -r requirements.txt` (**pip** = Paketmanager für Python, installiert benötigte Pakete).

Damit ist die Umgebung bereit für die Ausführung.

## Programm starten

1. `pytest` – führt die Tests aus.
2. `python src/main.py` – startet den Controller.
3. Mit `deactivate` verlässt du die virtuelle Umgebung.

## Weiterführende Befehle

* `git status` zeigt, welche Dateien geändert wurden.
* `git add <datei>` nimmt die Datei in den nächsten Commit (Versionsschritt) auf.
* `git commit -m "Nachricht"` speichert diesen Schritt lokal.
* `git push` sendet den Commit zum Server.

## Laien-Tipps

Weitere einfache Vorschläge stehen in `LAIENTIPPS.md`. Dort sind alle Befehle ausgeschrieben und Fachbegriffe (wie *Branch* oder *Server*) kurz erklärt.
Die Sammlung dort enthält jetzt auch Befehle wie `pwd`, `cat`, `nano`, `history`, `man`, `apt update`, `df -h`, `curl` und `wget` mit kurzen Erlaeuterungen.

Es gibt auch eine kleine grafische Oberflaeche. Mit `python src/gui.py` startest du sie und kannst den Controller per Knopfdruck aufrufen.
Die Tippsdatei enthaelt zudem neue Befehle wie `less`, `tail` und `ssh`.
Auch Befehle wie `free -m`, `whoami`, `ping` und `traceroute` sind nun erklaert.

## Best Practices

Eine ausführliche Liste von bewährten Verfahren findest du in [BESTPRACTICES.md](BESTPRACTICES.md). Dort wird erklärt, wie du einheitliche Standards einhältst und den Code barrierefrei gestaltest.

## Barrierefreiheit

- Nutze hohe Kontraste in der grafischen Oberfläche.
- Hinterlege für Bilder immer einen beschreibenden Alt-Text (Text für Bildschirmleser).
- Größere Schrift kannst du im Terminal meist mit `Strg` + `+` einstellen.

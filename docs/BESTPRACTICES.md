# Best Practices und globale Standards

Diese Datei sammelt bewährte Vorgehensweisen. Fachbegriffe stehen in Klammern und werden kurz erklärt.

## Struktur

- Halte dich an **PEP8** (Stil-Regeln für Python).
- Benutze `python3 -m venv venv` für eine virtuelle Umgebung (getrennter Arbeitsbereich).
- Dokumentiere Änderungen immer in `README.md` und im Ordner `docs`.

## Codequalität

- Füge zu jeder Funktion einen kurzen Kommentar hinzu.
- Lege Tests im Ordner `tests` ab und starte sie mit `pytest`.
- Nutze Werkzeuge wie `flake8` oder `ruff` (Linter = Programm zur Code-Prüfung).

## Barrierefreiheit

- Achte auf hohe Kontraste und gut lesbare Schriftarten.
- Hinterlege Alt-Texte (Beschreibung für Bilder) bei grafischen Elementen.
- Überprüfe mit einem Bildschirmleser wie `orca`, ob alles verständlich ist.

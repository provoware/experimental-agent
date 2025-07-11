# Weitere Schritte

Hier findest du einfache Vorschlaege (Tipps), um das Projekt zu erweitern.
Alle Befehle sind komplett angegeben. Fachbegriffe stehen in Klammern und werden erklaert.

## 1. Abhaengigkeiten installieren (Dependencies)
```bash
pip install -r requirements.txt
```
Damit holst du alle benoetigten Bibliotheken (Libraries).

## 2. Tests ausfuehren
```bash
pytest -q
```
So pruefst du, ob alles funktioniert.

## 3. Neues Modul anlegen
```bash
touch src/neues_modul.py
```
Damit erstellst du eine neue Datei fuer zusaetzliche Funktionen (Module).

## 4. Grafische Oberflaeche starten (GUI)
```bash
python src/gui.py
```
Damit oeffnest du ein kleines Fenster. GUI steht fuer *graphical user interface* (grafische Benutzeroberflaeche).

## 5. Code pruefen (Linting)
```bash
pip install pylint
pylint src/main.py
```
`pylint` untersucht den Code auf moegliche Fehler (Linting = automatische Codepruefung).

## 6. Code formatieren
```bash
pip install black
black src/main.py
```
`black` sorgt fuer eine einheitliche Formatierung (Formatierer = Werkzeug fuer sauberen Code).

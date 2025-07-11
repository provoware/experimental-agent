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

## 4. Fixe und Merge (Fehler beheben und zusammenfuehren)
```bash
git pull
git merge hauptzweig
```
Der erste Befehl holt aktuelle Daten vom Server (Server = zentrale Ablage). Mit dem zweiten fuehrst du deinen Arbeitszweig mit dem Hauptzweig zusammen (merge = zusammenfuehren).

Falls ein Konflikt (Konflikt = widerspruechliche Aenderungen) auftritt:
```bash
nano betroffene_datei
git add betroffene_datei
git commit -m "Konflikt behoben"
```
Danach kannst du den Merge mit `git push` abschliessen.

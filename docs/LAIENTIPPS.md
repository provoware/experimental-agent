# Laien-Tipps

Diese Datei sammelt einfache Vorschläge mit vollständigen Befehlen. Fachwörter stehen in Klammern und werden erklärt.

## Grundlegende Befehle

- `git pull` – holt die neuesten Änderungen vom Server (Server = zentrale Ablage des Projekts).
- `git branch neuer-zweig` – erstellt einen neuen Branch (Branch = Entwicklungszweig, parallele Arbeitslinie).
- `git checkout neuer-zweig` – wechselt auf diesen Branch.
- `git merge anderer-zweig` – fügt die Arbeit eines anderen Branches zusammen (merge = zusammenführen).
- `python beispiel.py` – führt ein Python-Programm aus (Python = Programmiersprache für dieses Projekt).
- `pip uninstall paketname` – entfernt ein Paket, das nicht mehr gebraucht wird (Paket = Sammlung von Programmteilen).
- `rm -r ordnername` – löscht einen Ordner samt Inhalt (Ordner = Verzeichnis).

Die Liste soll Einsteigern helfen, häufige Aufgaben selbstständig zu erledigen.
- `ls` – zeigt den Inhalt des aktuellen Ordners an (Ordner = Verzeichnis).
- `cd ..` – wechselt eine Ebene nach oben (Ebene = uebergeordneter Ordner).
- `mkdir neuerordner` – legt einen neuen Ordner an.
- `touch datei.txt` – erstellt eine leere Datei (Datei = einzelnes Dokument).
- `cp quelle ziel` – kopiert eine Datei (kopieren = duplizieren).
- `mv quelle ziel` – verschiebt oder benennt eine Datei um (verschieben = an anderen Ort legen).

## Weitere nuetzliche Befehle

- `pwd` – zeigt den aktuellen Pfad an (Pfad = Position im Dateisystem).
- `cat datei.txt` – gibt den Inhalt einer Datei aus (Inhalt = gespeicherter Text).
- `nano datei.txt` – oeffnet einen einfachen Editor (Editor = Programm zum Bearbeiten von Dateien).
- `grep wort datei.txt` – sucht nach einem Wort in einer Datei (suchen = durchsuchen nach Text).
- `python -m pip install paket` – installiert ein Paket ueber Python (Paket = Sammlung von Programmteilen).

## Weiterfuehrende Befehle

- `history` – zeigt die zuvor eingegebenen Befehle (History = Befehlsverlauf).
- `man befehl` – ruft die Handbuchseite auf (man = manual, Handbuch).
- `chmod +x datei.sh` – macht eine Datei ausfuehrbar (ausfuehrbar = kann gestartet werden).
- `tar -czf archiv.tar.gz ordner` – erstellt ein komprimiertes Archiv (Archiv = gepackte Datei).
- `sudo befehl` – fuehrt einen Befehl mit Administratorrechten aus (Administrator = Benutzer mit allen Rechten).

## Noch mehr nuetzliche Befehle

- `apt update && apt upgrade` – aktualisiert alle Pakete (Pakete = installierte Programme).
- `df -h` – zeigt wie voll die Festplatte ist (Festplatte = Speicher).
- `top` – listet laufende Programme in Echtzeit (Echtzeit = sofortige Aktualisierung).
- `ps aux` – zeigt alle laufenden Prozesse an (Prozess = laufendes Programm).
- `kill <PID>` – beendet einen Prozess (PID = Prozess-ID).
- `curl https://adresse` – ruft Daten aus dem Internet ab (Internet = weltweites Netzwerk).
- `wget <URL>` – laedt eine Datei herunter (herunterladen = aus dem Internet speichern).

## Noch weiterfuehrende Befehle

- `less datei.txt` – zeigt den Inhalt seitenweise an (seitenweise = blättern durch Text).
- `head -n 10 datei.txt` – zeigt die ersten Zeilen an (Zeile = Textreihe).
- `tail -n 10 datei.txt` – zeigt die letzten Zeilen an.
- `du -sh ordner` – zeigt, wie viel Speicher ein Ordner braucht (Speicher = Platz auf der Festplatte).
- `ip a` – listet Netzwerkinformationen auf (Netzwerk = Verbindung zwischen Computern).
- `ssh benutzer@host` – verbindet sich mit einem anderen Rechner (ssh = sichere Fernsteuerung).
- `scp datei benutzer@host:/pfad` – kopiert eine Datei zu einem anderen Rechner (kopieren = übertragen).

## Nuetzliche Systembefehle

- `free -m` – zeigt den freien Arbeitsspeicher an (Arbeitsspeicher = RAM).
- `uptime` – gibt an, wie lange der Rechner bereits laeuft (Rechner = Computer).
- `whoami` – zeigt den aktuellen Benutzer (Benutzer = Nutzerkonto).
- `which befehl` – nennt den Pfad zu einem Programm (Pfad = Speicherort).
- `uname -a` – liefert Details zum Betriebssystem (Betriebssystem = Grundsoftware).

## Netzwerkbefehle

- `ping adresse` – prueft die Verbindung zu einem Ziel (Ziel = andere Adresse im Netz).
- `traceroute adresse` – zeigt die Stationen bis zum Ziel (Stationen = Zwischenknoten).
- `sudo apt autoremove` – entfernt uebriggebliebene Pakete (Pakete = installierte Programme).
- `ssh-keygen` – erstellt Schluessel fuer sichere Verbindungen (Schluessel = digitales Passwort).

## Versionskontrolle erweitern

- `git log` – zeigt die Historie an (Historie = Liste aller Commits).
- `git stash` – legt Änderungen vorübergehend beiseite (beiseitelegen = speichern ohne Commit).

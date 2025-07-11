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
- `git revert HEAD` – macht den letzten Commit rückgängig (Commit = gespeicherter Arbeitsschritt), ohne die Historie zu verändern.
- `git reset --hard HEAD~1` – setzt den Stand um einen Commit zurück (Stand = aktueller Inhalt). Alle lokalen Änderungen gehen verloren.
- `git diff` – zeigt die aktuellen Unterschiede an (Unterschiede = Änderungen seit dem letzten Commit).
- `git cherry-pick <hash>` – übernimmt einen bestimmten Commit von einem anderen Zweig (Commit = gespeicherter Arbeitsschritt).
- `git tag -a v1.0 -m "Text"` – erstellt eine Markierung (Tag = fester Punkt in der Historie) mit Beschreibung.

## Noch mehr Versionskontrolle

- `git rebase main` – wendet deine Arbeit auf die aktuelle Hauptlinie an (rebase = neu ausrichten).
- `git commit --amend` – ändert den letzten Commit (Commit = gespeicherter Arbeitsschritt) nachträglich.
- `git bisect start` – hilft einen Fehler schnell zu finden (bisect = halbieren).
- `git bisect good <hash>` – markiert eine Version ohne Fehler.
- `git bisect bad <hash>` – markiert eine Version mit dem Fehler.
- `git clean -f` – entfernt unversionierte Dateien (unversioniert = nicht in Git).
- `git remote add origin <URL>` – verbindet dein Projekt mit einem Server (Server = zentrale Ablage).
- `git push origin main` – überträgt deine Arbeit zum Server.

## Professionelle Versionskontrolle

- `git fetch origin` – holt neue Daten vom Server, ohne sie einzubauen (fetch = nur herunterladen).
- `git pull --rebase` – holt Daten und ordnet deine Arbeit oben an (rebase = neu ausrichten).
- `git branch -d zweig` – löscht einen Entwicklungszweig (Branch = parallele Arbeitslinie).
- `git merge --no-ff zweig` – fügt einen Zweig immer als eigenen Punkt ein (no-ff = ohne direkte Verschmelzung).
- `git remote -v` – zeigt verbundene Server an (remote = entfernte Ablage).
- `git stash list` – zeigt abgelegte Änderungen (stash = Zwischenablage).
- `git stash pop` – holt zuletzt abgelegte Änderungen zurück (pop = wiederherstellen).
- `git rebase --abort` – bricht eine laufende Rebase ab (Rebase = Neuordnung der Commits).
- `git merge --abort` – bricht einen Merge-Vorgang ab (Merge = Zusammenführen).
- `git branch -m alt neu` – benennt einen Zweig um.
- `git config --global user.name "Name"` – legt deinen Namen fest (Config = Einstellung).
- `git config --global user.email "mail@example.com"` – legt deine E-Mail fest.

## Profi-Version

- `git reflog` – listet alle Bewegungen des Projektzeigers auf (reflog = Verlauf der Commits) und hilft, verlorene Stände wiederzufinden.
- `git submodule add <URL> unterordner` – bindet ein weiteres Repository ein (Submodule = eingebettetes Unterprojekt).
- `git worktree add -b zweig ../zweig-verzeichnis` – legt einen zusätzlichen Arbeitsbaum an (Worktree = weiterer Projektordner) und erstellt direkt einen neuen Zweig.
- `git commit --signoff -m "Nachricht"` – fügt dem Commit eine Signaturzeile hinzu (Signoff = Bestätigung mit Namen und E-Mail).
- `git gc` – räumt das Repository auf (gc = garbage collection, Datenbereinigung).
- `git blame datei` – zeigt, wer welche Zeile zuletzt geändert hat (blame = Zuschreibung).

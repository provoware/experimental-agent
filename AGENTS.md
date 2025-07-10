# AGENTS.md – Umfassendes Beispiel

## Projektvision
Das Hauptmodul ist der unveränderliche zentrale Controller des Systems. Es wird über eine grafische Benutzeroberfläche gesteuert und verfügt über Selbstheilungsmechanismen.

## Verzeichnisstruktur
- Zu Beginn wird eine vollständige Platzhalter-Baumstruktur angelegt.
- Dateien tragen im Namen ihren Status: `.todo` für noch zu erledigende, `.done` für fertige.
- Die Datei `verzeichnisstruktur.txt` wird bei jeder Iteration automatisch neu generiert und zeigt den aktuellen Stand an.

## Logging & CLI-Übersicht
- **actions.log**: Protokolliert Datum, betroffene Datei und genaue Aktion.
- **commands.txt**: Listet alle CLI-Befehle mit Kontext und kurzer Nutzungsanleitung.

## Selbstheilung & Rollback
- Automatische Erkennung und Behebung von Fehlern im Hauptmodul.
- Rollback erfolgt über statusgekennzeichnete Kopien im Backup-Ordner oder anhand des Dateinamens.

## Iteration & Automatisierung
1. **Fehlende Dateien prüfen**  
   - Jeder Iterationsschritt validiert den vollständigen Dateibaum.  
   - Falls eine Datei fehlt, wird mindestens eine neue `.todo`-Datei gemäß Vorgabe angelegt.

2. **Änderungen anwenden**  
   - Modifikationen werden über Codex online vorgenommen und lokal nur zum Test geklont.  
   - Nach bestandenem Test werden sie automatisch ins GitHub-Repository gemergt.

3. **Dokumentation der Fortschritte**  
   - In **info.txt** steht jeweils der letzte ausgeführte und der nächste anstehende Schritt.

4. **Release-Fertigkeit sicherstellen**  
   - Am Ende aller Iterationen liegt ein lauffähiges Linux-AppImage vor, das portabel ist und nur durch Hinzufügen neuer Module erweitert werden kann.

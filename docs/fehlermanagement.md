# Selbstheilung und Fehlertoleranz

Dieses Dokument erklaert einfach, wie der Controller (Steuerprogramm) mit Fehlern umgeht.

## Selbstheilung (self healing)
- Der Controller prueft automatisch, ob Module noch richtig laufen.
- Falls ein Problem erkannt wird, startet er das betroffene Modul neu.
- Bei kleineren Fehlern versucht er, diese direkt zu beheben.

## Fehlertoleranz (fault tolerance)
- Wenn ein Modul ausfaellt, laeuft der Rest des Systems weiter.
- So bleibt das Programm insgesamt funktionsfaehig, auch wenn einzelne Teile kurzzeitig Probleme haben.

## Intelligentes Fehlermanagement
- Alle Schritte werden in `actions.log` gespeichert (Log = Protokolldatei).
- Das System fuehrt bei Bedarf automatisch ein Rollback (Ruecksprung) auf eine fruehere Version durch.
- Nach einem Fehler laesst sich per `pytest` schnell testen, ob alles wieder funktioniert.

## Befehle fuer Einsteiger
- `systemctl status dienst` – zeigt den Zustand eines Dienstes (Dienst = Hintergrundprogramm).
- `journalctl -xe` – gibt aktuelle Systemnachrichten aus (Systemjournal = zentrale Logdatei).
- `dmesg` – listet Meldungen des Kernels (Kernel = Kern des Betriebssystems).
- `tail -f /var/log/syslog` – verfolgt laufend das Systemprotokoll.

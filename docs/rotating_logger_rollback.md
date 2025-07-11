# Rotierendes Logging und Rollback

Dieses Dokument erklaert in einfacher Sprache, wie man einen rotierenden Logger (Logdatei-Wechsler) und ein Rollback (Ruecksetzen auf einen frueheren Zustand) nutzt.

## Logger einrichten

1. **Bibliothek** `logging` benutzen.
2. Einen `RotatingFileHandler` (rotierender Dateibehandler) erstellen. Dieser legt automatisch neue Logdateien an, wenn eine Datei zu gross wird.
3. Beispielcode:
   ```python
   from logging.handlers import RotatingFileHandler
   handler = RotatingFileHandler("controller.log", maxBytes=10000, backupCount=1)
   logger.addHandler(handler)
   ```
   - `maxBytes` bestimmt die maximale Groesse der Logdatei in Bytes.
   - `backupCount` gibt an, wie viele alte Dateien behalten werden.
4. Der Logger schreibt dann Meldungen mit `logger.info("Text")` in die Datei `controller.log`.

## Rollback einsetzen

1. Aktionen in einen `try`-Block (Versuch) packen.
2. Falls ein Fehler auftritt (`except`), den alten Zustand wiederherstellen und eine Meldung ausgeben.
3. Beispiel:
   ```python
   try:
       kritische_operation()
   except Exception as fehler:
       logger.error("Fehler aufgetreten: %s", fehler)
       zustand_zuruecksetzen()
   ```
   Dabei speichert `kritische_operation()` den neuen Zustand nur, wenn alles klappt.

## Kompletter Ablauf

Der Controller im Projekt zeigt diesen Ablauf in der Methode `run_safe()`.

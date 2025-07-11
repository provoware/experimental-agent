# Release erstellen

Dieses Projekt nutzt **python-semantic-release**. Damit wird anhand der Git-Historie automatisch eine neue Version erstellt und ein Changelog erzeugt.

## Schritt-für-Schritt-Anleitung

1. `pip install python-semantic-release` (installiert das Paket)
2. `semantic-release changelog` (erstellt die Datei `CHANGELOG.md` aus den Commit-Nachrichten)
3. `semantic-release version` (erhöht die Versionsnummer automatisch)
4. `git push && git push --tags` (lädt Änderungen und Tags hoch)

Begriffe in Klammern:
- **Version** (Versionsnummer): Nummer, die den Entwicklungsstand beschreibt, z.B. 1.0.0.
- **Commit** (gespeicherte Änderung): Eine Einheit von Änderungen im Git-Verlauf.


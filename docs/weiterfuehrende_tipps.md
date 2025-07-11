# Weiterführende Tipps für Einsteiger

In diesem Abschnitt findest du einfache Hinweise, wie du das Projekt erweitern kannst. Die verwendeten Fachbegriffe stehen jeweils in Klammern und werden kurz erläutert.

## Projekt starten

1. **Abhängigkeiten installieren**

   ```bash
   pip install -e .[dev]
   ```

   *`pip` ist das Installationswerkzeug für Python-Pakete. Mit `-e` (editable) kannst du den Quellcode direkt bearbeiten. Der Zusatz `[dev]` installiert die Pakete aus dem Bereich *Entwicklung* (Extras für Entwickler).* 

2. **Tests ausführen**

   ```bash
   pytest
   ```

   *`pytest` ist ein Testwerkzeug. Es prüft automatisch, ob dein Code wie erwartet funktioniert.*

3. **Code formatieren**

   ```bash
   black src tests
   ```

   *`black` formatiert den Code nach einheitlichen Regeln. Das macht ihn leichter lesbar.*

Diese Befehle gibst du im Terminal (Eingabeaufforderung) ein. So behältst du die Kontrolle über deine Entwicklungsumgebung.

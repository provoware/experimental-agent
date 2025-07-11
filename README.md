# experimental-agent

## English

This project demonstrates an **immutable** (unchangeable) central controller. It can be operated via a simple interface.

### Quick Start

1. **Clone the repository**:
   ```bash
   git clone <REPO-URL>
   cd experimental-agent
   ```
2. **Run the tests** (small programs that check the code):
   ```bash
   pytest
   ```
3. **Start the controller**:
   ```bash
   python src/main.py
   ```

### Usage Examples

- Print the greeting from `hauptfunktion`:
  ```bash
  python -c "from src.main import hauptfunktion; print(hauptfunktion())"
  ```

### Additional Tips for Beginners

- Create a **virtual environment** (isolated Python workspace) with:
  ```bash
  python -m venv venv
  source venv/bin/activate
  ```
- Install dependencies (required packages) if a `requirements.txt` file exists:
  ```bash
  pip install -r requirements.txt
  ```

## Deutsch

Dieses Projekt zeigt einen **unveränderlichen** (nicht veränderbaren) zentralen Controller. Er lässt sich über eine einfache Oberfläche steuern.

### Schnellstart

1. **Repository klonen** (Kopie anlegen):
   ```bash
   git clone <REPO-URL>
   cd experimental-agent
   ```
2. **Tests ausführen** (kleine Programme zum Prüfen des Codes):
   ```bash
   pytest
   ```
3. **Controller starten**:
   ```bash
   python src/main.py
   ```

### Anwendungsbeispiele

- Grußnachricht über `hauptfunktion` ausgeben:
  ```bash
  python -c "from src.main import hauptfunktion; print(hauptfunktion())"
  ```

### Weiterführende Tipps für Einsteiger

- Eine **virtuelle Umgebung** (eigener Arbeitsbereich für Python) anlegen:
  ```bash
  python -m venv venv
  source venv/bin/activate
  ```
- Abhängigkeiten (benötigte Zusatzprogramme) installieren, falls es eine `requirements.txt` gibt:
  ```bash
  pip install -r requirements.txt
  ```

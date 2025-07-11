import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from main import Controller, hauptfunktion


def test_run_returns_message():
    c = Controller()
    assert c.run() == "Controller laeuft"


def test_hauptfunktion():
    assert hauptfunktion() == "Hallo Welt"


def test_hauptfunktion_typ():
    ergebnis = hauptfunktion()
    assert isinstance(ergebnis, str)


def test_hauptfunktion_laenge():
    ergebnis = hauptfunktion()
    assert len(ergebnis) > 0


def test_cli_execution(tmp_path):
    result = subprocess.run([
        sys.executable,
        str(Path(__file__).resolve().parents[1] / "src" / "main.py"),
    ], capture_output=True, text=True, check=True)
    assert "Controller laeuft" in result.stdout

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.main import Controller, hauptfunktion


def test_run_returns_message() -> None:
    controller = Controller()
    assert controller.run() == "Controller laeuft"


def test_hauptfunktion() -> None:
    assert hauptfunktion() == "Hallo Welt"


def test_hauptfunktion_typ() -> None:
    ergebnis = hauptfunktion()
    assert isinstance(ergebnis, str)


def test_hauptfunktion_laenge() -> None:
    ergebnis = hauptfunktion()
    assert len(ergebnis) > 0

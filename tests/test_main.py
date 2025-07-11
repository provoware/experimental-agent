import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.main import Controller, hauptfunktion


def test_run_returns_message() -> None:
    c = Controller()
    assert c.run() == "Controller laeuft"


def test_hauptfunktion() -> None:
    assert hauptfunktion() == "Hallo Welt"


def test_hauptfunktion_typ() -> None:
    assert isinstance(hauptfunktion(), str)


def test_hauptfunktion_laenge() -> None:
    assert len(hauptfunktion()) > 0

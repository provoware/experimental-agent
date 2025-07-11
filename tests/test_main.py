import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from main import Controller, hauptfunktion


def test_run_returns_message():
    c = Controller()
    assert c.run() == "Controller laeuft"

def test_self_heal():
    c = Controller()
    assert c.self_heal() == "Selbstheilung aktiviert"


def test_hauptfunktion():
    assert hauptfunktion() == "Hallo Welt"


def test_hauptfunktion_typ():
    ergebnis = hauptfunktion()
    assert isinstance(ergebnis, str)


def test_hauptfunktion_laenge():
    ergebnis = hauptfunktion()
    assert len(ergebnis) > 0

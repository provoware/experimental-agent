import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import Controller, hauptfunktion


def test_run_returns_message():
    c = Controller()
    assert c.run() == "Controller laeuft"

def test_self_heal():
    c = Controller()
    assert c.self_heal() == "Selbstheilung aktiviert"


def test_add_module_success():
    c = Controller()
    assert c.add_module("math") == "Modul math geladen"


def test_add_module_placeholder(tmp_path):
    c = Controller()
    module_name = "temp_test_mod"
    path = os.path.join("src", f"{module_name}.py")
    if os.path.exists(path):
        os.remove(path)
    msg = c.add_module(module_name)
    assert "Platzhalter" in msg
    assert os.path.exists(path)
    os.remove(path)

def test_hauptfunktion():
    assert hauptfunktion() == "Hallo Welt"


def test_hauptfunktion_typ():
    ergebnis = hauptfunktion()
    assert isinstance(ergebnis, str)


def test_hauptfunktion_laenge():
    ergebnis = hauptfunktion()
    assert len(ergebnis) > 0

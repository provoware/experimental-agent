import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

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


def test_controller_inherits_globalsettings():
    c = Controller()
    assert hasattr(c, 'theme')


def test_dashboard_structure():
    c = Controller()
    assert hasattr(c.dashboard, 'header')
    assert hasattr(c.dashboard, 'left_sidebar')
    assert hasattr(c.dashboard, 'right_sidebar')
    assert len(c.dashboard.footer.columns) == 4


def test_dashboard_overview():
    c = Controller()
    info = c.dashboard.overview()
    assert info["header"] == "Dashboard"
    assert isinstance(info["footer"], list)
    assert len(info["footer"]) == 4


import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import hauptfunktion


def test_hauptfunktion():
    assert hauptfunktion() == "Hallo Welt"

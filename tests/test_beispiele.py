import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.beispiele import begruesse


def test_begruesse_antwort():
    assert begruesse("Bob") == "Hallo Bob"

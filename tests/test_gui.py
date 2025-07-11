import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from gui import gui_message


def test_gui_message():
    assert gui_message() == "GUI bereit"

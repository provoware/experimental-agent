import os
from pathlib import Path
from typing import Any
from unittest import mock

import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.modules.settings import backend


def test_round_trip(tmp_path: Path) -> None:
    test_file = tmp_path / "conf.yaml"
    with mock.patch.object(backend, "SETTINGS_FILE", test_file):
        data = {"theme": "dark", "font_size": "L"}
        backend.save_settings(data)
        loaded = backend.load_settings()
        assert loaded == data


def test_load_defaults(tmp_path: Path) -> None:
    test_file = tmp_path / "conf.yaml"
    with mock.patch.object(backend, "SETTINGS_FILE", test_file):
        loaded = backend.load_settings()
        assert loaded == backend.DEFAULT_SETTINGS


def test_gui_instantiation(monkeypatch: Any) -> None:
    os.environ["QT_QPA_PLATFORM"] = "offscreen"
    from src.modules.settings.gui import SettingsWindow

    win = SettingsWindow()
    win.close()

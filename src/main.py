"""Hauptmodul."""

from __future__ import annotations

import os
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow

from .modules.settings.gui import SettingsWindow


class Controller:
    """Unveraenderlicher zentraler Controller."""

    def __init__(self) -> None:
        self._running = False

    def run(self) -> str:
        """Starte den Controller und gebe eine Meldung zurueck."""
        self._running = True
        return "Controller laeuft"


def hauptfunktion() -> str:
    """Gibt eine Grußnachricht zurück."""
    return "Hallo Welt"


class MainWindow(QMainWindow):
    """Hauptfenster mit Zugang zu den Einstellungen."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Experimental Agent")
        self._settings_window: SettingsWindow | None = None

        settings_action = QAction("Einstellungen...", self)
        settings_action.triggered.connect(self.open_settings)
        self.menuBar().addAction(settings_action)

    def open_settings(self) -> None:
        if self._settings_window is None:
            self._settings_window = SettingsWindow()
        self._settings_window.show()


def start_gui() -> None:
    """Starte die grafische Oberfläche."""
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    print(Controller().run())

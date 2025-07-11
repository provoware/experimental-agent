from __future__ import annotations

import os
from typing import Dict

from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QSlider,
    QVBoxLayout,
    QWidget,
)
from PySide6.QtCore import Qt

from .backend import DEFAULT_SETTINGS, load_settings, save_settings


class SettingsWindow(QWidget):
    def __init__(self) -> None:
        # ensure headless operation if needed
        os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
        if QApplication.instance() is None:
            QApplication([])
        super().__init__()
        self.setWindowTitle("Einstellungen")
        self.settings: Dict[str, str] = load_settings()

        layout = QVBoxLayout(self)

        self.theme_box = QCheckBox("Dark Mode")
        self.theme_box.setChecked(self.settings["theme"] == "dark")
        self.theme_box.stateChanged.connect(self._on_theme_change)
        layout.addWidget(self.theme_box)

        self.size_label = QLabel(self.settings["font_size"])
        layout.addWidget(self.size_label)

        self.size_slider = QSlider(Qt.Horizontal)  # type: ignore[attr-defined]
        self.size_slider.setMinimum(0)
        self.size_slider.setMaximum(4)
        self.size_slider.setValue(self._font_to_value(self.settings["font_size"]))
        self.size_slider.valueChanged.connect(self._on_size_change)
        layout.addWidget(self.size_slider)

        self.apply_settings()

    def _on_theme_change(self, state: int) -> None:
        self.settings["theme"] = "dark" if state == Qt.Checked else "light"  # type: ignore[attr-defined]
        save_settings(self.settings)
        self.apply_settings()

    def _on_size_change(self, value: int) -> None:
        font_key = self._value_to_font(value)
        self.settings["font_size"] = font_key
        self.size_label.setText(font_key)
        save_settings(self.settings)
        self.apply_settings()

    def _font_to_value(self, key: str) -> int:
        mapping = {"XS": 0, "S": 1, "M": 2, "L": 3, "XL": 4}
        return mapping.get(key, 2)

    def _value_to_font(self, value: int) -> str:
        mapping = {0: "XS", 1: "S", 2: "M", 3: "L", 4: "XL"}
        return mapping.get(value, DEFAULT_SETTINGS["font_size"])

    def apply_settings(self) -> None:
        if self.settings["theme"] == "dark":
            self.setStyleSheet("background-color:#333333;color:#ffffff;")
        else:
            self.setStyleSheet("")
        size_map = {"XS": 8, "S": 10, "M": 12, "L": 14, "XL": 16}
        font_size = size_map.get(self.settings["font_size"], 12)
        self.setStyleSheet(self.styleSheet() + f"font-size:{font_size}pt;")

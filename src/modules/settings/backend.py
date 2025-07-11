from __future__ import annotations

from pathlib import Path
from typing import Dict

import yaml

SETTINGS_FILE = Path.home() / ".experimental_agent.yaml"

DEFAULT_SETTINGS: Dict[str, str] = {"theme": "light", "font_size": "M"}


def load_settings() -> Dict[str, str]:
    if SETTINGS_FILE.exists():
        with SETTINGS_FILE.open("r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        if not isinstance(data, dict):
            data = {}
    else:
        data = {}
    result = {**DEFAULT_SETTINGS, **{k: str(v) for k, v in data.items()}}
    return result


def save_settings(settings: Dict[str, str]) -> None:
    SETTINGS_FILE.write_text(yaml.safe_dump(settings), encoding="utf-8")

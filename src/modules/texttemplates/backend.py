import os
import yaml
import pyperclip

DEFAULT_PATH = os.path.expanduser('~/.experimental_agent_templates.yaml')


class TemplateManager:
    """Manage text templates stored in a YAML file."""

    def __init__(self, path: str = DEFAULT_PATH):
        self.path = path
        self.templates = {}
        self._load()

    def _load(self) -> None:
        if os.path.exists(self.path):
            with open(self.path, 'r', encoding='utf-8') as f:
                self.templates = yaml.safe_load(f) or {}
        else:
            self.templates = {}

    def _save(self) -> None:
        with open(self.path, 'w', encoding='utf-8') as f:
            yaml.safe_dump(self.templates, f)

    def list_templates(self):
        return list(self.templates.items())

    def add_or_update(self, name: str, content: str) -> None:
        self.templates[name] = content
        self._save()

    def delete(self, name: str) -> None:
        if name in self.templates:
            del self.templates[name]
            self._save()

    def get(self, name: str) -> str:
        return self.templates.get(name, '')

    def copy_to_clipboard(self, name: str) -> None:
        text = self.get(name)
        pyperclip.copy(text)

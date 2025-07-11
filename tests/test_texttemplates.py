import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)

import pyperclip  # noqa: E402

from src.modules.texttemplates.backend import TemplateManager  # noqa: E402


def test_persistence(tmp_path):
    path = tmp_path / 'templates.yaml'
    mgr = TemplateManager(path=str(path))
    mgr.add_or_update('a', 'b')
    mgr2 = TemplateManager(path=str(path))
    assert mgr2.get('a') == 'b'


def test_clipboard_copy(monkeypatch, tmp_path):
    path = tmp_path / 'templates.yaml'
    mgr = TemplateManager(path=str(path))
    mgr.add_or_update('x', 'y')
    copied = []
    monkeypatch.setattr(pyperclip, 'copy', lambda text: copied.append(text))
    mgr.copy_to_clipboard('x')
    assert copied == ['y']


def test_crud(tmp_path):
    path = tmp_path / 'templates.yaml'
    mgr = TemplateManager(path=str(path))
    mgr.add_or_update('name', 'one')
    mgr.add_or_update('name', 'two')
    assert mgr.get('name') == 'two'
    mgr.delete('name')
    assert mgr.get('name') == ''

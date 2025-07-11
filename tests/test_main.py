import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import Controller

def test_run_returns_message():
    c = Controller()
    assert c.run() == "Controller laeuft"

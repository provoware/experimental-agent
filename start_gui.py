#!/usr/bin/env python3
"""Startskript fuer die grafische Oberflaeche."""
import subprocess
import sys

from src.gui import start_gui, gui_message


def run_tests():
    """Fuehrt die vorhandenen Tests aus."""
    try:
        subprocess.check_call([sys.executable, "-m", "pytest", "-q"])
        return True
    except subprocess.CalledProcessError:
        return False


def self_heal():
    """Versucht, einfache Fehler zu beheben."""
    try:
        from src.main import Controller
        c = Controller()
        c.self_heal()
        return True
    except Exception:
        return False


def main():
    if not run_tests():
        print("Tests fehlgeschlagen. Versuche Selbstheilung...")
        if self_heal():
            print("Selbstheilung durchgefuehrt.")
        else:
            print("Selbstheilung fehlgeschlagen.")
    app = start_gui()
    print(gui_message())
    app.mainloop()


if __name__ == "__main__":
    main()

class Controller:
    """Unveränderlicher zentraler Controller."""

    def __init__(self):
        self._running = False

    def run(self) -> str:
        """Starte den Controller und gebe eine Meldung zurück."""
        self._running = True
        return "Controller läuft"


def hauptfunktion() -> str:
    """Gibt eine Grußnachricht zurück."""
    return "Hallo Welt"


if __name__ == "__main__":
    print(Controller().run())

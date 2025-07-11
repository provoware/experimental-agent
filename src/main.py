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


if __name__ == "__main__":
    print(Controller().run())

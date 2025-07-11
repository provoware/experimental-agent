import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("controller")
handler = RotatingFileHandler("controller.log", maxBytes=10000, backupCount=1)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

class Controller:
    """Unveraenderlicher zentraler Controller."""

    def __init__(self):
        self._running = False

    def run(self):
        """Starte den Controller und gebe eine Meldung zurueck."""
        self._running = True
        logger.info("Controller gestartet")
        return "Controller laeuft"

    def run_safe(self):
        """Beispiel fuer Fehlerbehandlung mit Rollback."""
        self._running = True
        try:
            logger.info("Operation gestartet")
            # Platzhalter, der einen Fehler ausloest
            raise RuntimeError("Fehler im System")
        except Exception as e:
            logger.error("Fehler aufgetreten: %s. Rollback ausgefuehrt.", e)
            self._running = False
            return "Rollback ausgefuehrt"
        return "Controller laeuft"


def hauptfunktion():
    """Gibt eine Grußnachricht zurueck."""
    return "Hallo Welt"


if __name__ == "__main__":
    print(Controller().run())

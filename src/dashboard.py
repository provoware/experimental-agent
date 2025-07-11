from globalsettings import GlobalSettings


class DashboardHeader:
    """Einfacher Kopfbereich (Header) des Dashboards."""

    def __init__(self, title: str = "Dashboard"):
        self.title = title


class Sidebar:
    """Aufklappbare Seitenleiste."""

    def __init__(self, side: str):
        self.side = side
        self.collapsed = True

    def toggle(self) -> None:
        """Seitenleiste auf- oder zuklappen."""
        self.collapsed = not self.collapsed


class Footer:
    """Vierspaltiger Fussbereich."""

    def __init__(self):
        self.columns = ["Logging", "Debugging", "Daten", "Informationen"]


class Dashboard(GlobalSettings):
    """Dashboard mit Kopf, zwei Seitenleisten und Fuss."""

    def __init__(self, title: str = "Dashboard"):
        super().__init__()
        self.header = DashboardHeader(title)
        self.left_sidebar = Sidebar("links")
        self.right_sidebar = Sidebar("rechts")
        self.footer = Footer()


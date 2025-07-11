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

    def overview(self) -> dict:
        """Gibt eine einfache Übersicht des Dashboards zurück."""
        return {
            "header": self.header.title,
            "left_sidebar_open": not self.left_sidebar.collapsed,
            "right_sidebar_open": not self.right_sidebar.collapsed,
            "footer": self.footer.columns,
        }


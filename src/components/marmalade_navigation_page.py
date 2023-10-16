from gi.repository import Adw, Gtk


class MarmaladeNavigationPage(Adw.NavigationPage):
    """Abstract base class to use for navigation pages"""

    __gtype_name__ = "MarmaladeNavigationPage"

    navigation: Adw.NavigationView
    window: Gtk.Window

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.connect("realize", self.__on_realized)

    def __on_realized(self, _page) -> None:
        """Code called when the widget is going to be drawn"""
        self.navigation = self.get_parent()
        self.window = self.get_root()

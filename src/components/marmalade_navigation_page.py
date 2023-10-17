from gi.repository import Adw, Gtk

# TODO Not being a template, this class' children throw an error.
# gtk_widget_init_template: assertion 'template != NULL' failed
# Note that this class cannot have a template, nested templates are not supported.


class MarmaladeNavigationPage(Adw.NavigationPage):
    """Abstract base class to use for navigation pages"""

    __gtype_name__ = "MarmaladeNavigationPage"

    navigation: Adw.NavigationView

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.connect("realize", self.__on_realized)

    def __on_realized(self, _page) -> None:
        """Code called when the widget is going to be drawn"""
        self.navigation = self.get_parent()

from gi.repository import Adw


class AbcNavigationPage(Adw.NavigationPage):
    """Abstract base class to use for navigation pages"""

    _navigation: Adw.NavigationView

    def __init__(self, *args, navigation: Adw.NavigationView, **kwargs) -> None:
        """
        Create a base navigation page, used for app views

        Pages need to access their NavigationView parent to pop themselves
        and push pages programmatically at runtime.
        """
        super().__init__(*args, **kwargs)
        self._navigation = navigation

from functools import partial
from typing import Callable

from gi.repository import Adw, GLib, GObject

from src.components.server_browser import ServerBrowser
from src.components.server_browser_headerbar import ServerBrowserHeaderbar


class ServerPage(Adw.NavigationPage):
    """Base class for server pages"""

    __gtype_name__ = "MaramaladeServerPage"

    # browser property

    __browser: ServerBrowser

    @GObject.Property(type=object)
    def browser(self) -> ServerBrowser:
        return self.__browser

    def get_browser(self) -> ServerBrowser:
        return self.get_property("browser")

    @browser.setter
    def browser(self, value: ServerBrowser) -> None:
        self.__browser = value

    def set_browser(self, value: ServerBrowser):
        self.set_property("browser", value)

    # headerbar property

    __headerbar: ServerBrowserHeaderbar

    @GObject.Property(type=object)
    def headerbar(self) -> ServerBrowserHeaderbar:
        return self.__headerbar

    def get_headerbar(self) -> ServerBrowserHeaderbar:
        return self.get_property("headerbar")

    @headerbar.setter
    def headerbar(self, value: ServerBrowserHeaderbar) -> None:
        self.__headerbar = value

    def set_headerbar(self, value: ServerBrowserHeaderbar):
        self.set_property("headerbar", value)

    # is_filterable property

    __is_filterable: bool

    @GObject.Property(type=bool, default=False)
    def is_filterable(self) -> bool:
        return self.__is_filterable

    def get_is_filterable(self) -> bool:
        return self.get_property("is_filterable")

    @is_filterable.setter
    def is_filterable(self, value: bool) -> None:
        self.__is_filterable = value

    def set_is_filterable(self, value: bool):
        self.set_property("is_filterable", value)

    # is_root property

    __is_root: bool

    @GObject.Property(type=bool, default=False)
    def is_root(self) -> bool:
        return self.__is_root

    def get_is_root(self) -> bool:
        return self.get_property("is_root")

    @is_root.setter
    def is_root(self, value: bool) -> None:
        self.__is_root = value

    def set_is_root(self, value: bool):
        self.set_property("is_root", value)

    # Protected methods

    def _run_in_main_loop(self, func: Callable, *args, **kwargs) -> None:
        """Run a function with args and kwargs in the main loop"""
        partial_func = partial(func, *args, **kwargs)
        GLib.idle_add(partial_func)

    # Public methods

    def __init__(
        self,
        *args,
        browser: ServerBrowser,
        headerbar: ServerBrowserHeaderbar,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.set_browser(browser)
        self.set_headerbar(headerbar)

    def load(self) -> None:
        """Load the page content"""

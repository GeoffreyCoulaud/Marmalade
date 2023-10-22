from gi.repository import GObject

from src.components.server_browser import ServerBrowser
from src.components.server_browser_headerbar import ServerBrowserHeaderbar


class ServerPage(GObject.Object):
    """Base class for server pages"""

    def __init__(
        self,
        *args,
        browser: ServerBrowser,
        headerbar: ServerBrowserHeaderbar,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.__browser = browser
        self.__headerbar = headerbar

    # browser property

    __browser: ServerBrowser

    def set_browser(self, browser: ServerBrowser):
        self.__browser = browser

    def get_browser(self) -> ServerBrowser:
        return self.__browser

    @GObject.Property(type=object)
    def browser(self) -> ServerBrowser:
        return self.get_browser()

    @browser.setter
    def browser(self, value: ServerBrowser) -> None:
        self.set_browser(value)

    # headerbar property

    __headerbar: ServerBrowserHeaderbar

    def set_headerbar(self, headerbar: ServerBrowserHeaderbar):
        self.__headerbar = headerbar

    def get_headerbar(self) -> ServerBrowserHeaderbar:
        return self.__headerbar

    @GObject.Property(type=object)
    def headerbar(self) -> ServerBrowserHeaderbar:
        return self.get_headerbar()

    @headerbar.setter
    def headerbar(self, value: ServerBrowserHeaderbar) -> None:
        self.set_headerbar(value)

    # is_searchable property

    __is_searchable: bool

    def set_is_searchable(self, is_searchable: bool):
        self.__is_searchable = is_searchable

    def get_is_searchable(self) -> bool:
        return self.__is_searchable

    @GObject.Property(type=bool, default=False)
    def is_searchable(self) -> bool:
        return self.get_is_searchable()

    @is_searchable.setter
    def is_searchable(self, value: bool) -> None:
        self.set_is_searchable(value)

    # is_filterable property

    __is_filterable: bool

    def set_is_filterable(self, is_filterable: bool):
        self.__is_filterable = is_filterable

    def get_is_filterable(self) -> bool:
        return self.__is_filterable

    @GObject.Property(type=bool, default=False)
    def is_filterable(self) -> bool:
        return self.get_is_filterable()

    @is_filterable.setter
    def is_filterable(self, value: bool) -> None:
        self.set_is_filterable(value)

    # title property

    __title: str

    def set_title(self, title: str):
        self.__title = title
        self.__headerbar.set_title(title)

    def get_title(self) -> str:
        return self.__title

    @GObject.Property(type=str, default="")
    def title(self) -> str:
        return self.get_title()

    @title.setter
    def title(self, value: str) -> None:
        self.set_title(value)

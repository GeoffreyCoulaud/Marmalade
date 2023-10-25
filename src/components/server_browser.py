from gi.repository import Adw, Gio, GLib, GObject

from src.jellyfin import JellyfinClient


class ServerBrowser(Adw.NavigationPage):
    """Base class representing a server browser"""

    __gtype_name__ = "MarmaladeServerBrowser"

    def __init__(self, *args, client: JellyfinClient, user_id: str, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.set_client(client)
        self.set_user_id(user_id)

    # client property

    __client: JellyfinClient

    @GObject.Property(type=object)
    def client(self) -> JellyfinClient:
        return self.__client

    def get_client(self) -> JellyfinClient:
        return self.get_property("client")

    @client.setter
    def client(self, value: JellyfinClient) -> None:
        self.__client = value

    def set_client(self, value: JellyfinClient):
        self.set_property("client", value)

    # user_id property

    __user_id: str

    @GObject.Property(type=str)
    def user_id(self) -> str:
        return self.__user_id

    def get_user_id(self) -> str:
        return self.get_property("user_id")

    @user_id.setter
    def user_id(self, value: str) -> None:
        self.__user_id = value

    def set_user_id(self, value: str):
        self.set_property("user_id", value)

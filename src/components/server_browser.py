from gi.repository import Adw, Gio, GLib, GObject

from src.jellyfin import JellyfinClient


class ServerBrowser(GObject.Object):
    """Base class representing a server browser"""

    def __init__(self, *args, client: JellyfinClient, user_id: str, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.set_client(client)
        self.set_user_id(user_id)

    # client property

    __client: JellyfinClient

    def set_client(self, client: JellyfinClient):
        self.__client = client

    def get_client(self) -> JellyfinClient:
        return self.__client

    @GObject.Property(type=object)
    def client(self) -> JellyfinClient:
        return self.get_client()

    @client.setter
    def client(self, value: JellyfinClient) -> None:
        self.set_client(value)

    # user_id property

    __user_id: str

    def set_user_id(self, user_id: str):
        self.__user_id = user_id

    def get_user_id(self) -> str:
        return self.__user_id

    @GObject.Property(type=str, default="")
    def user_id(self) -> str:
        return self.get_user_id()

    @user_id.setter
    def user_id(self, value: str) -> None:
        self.set_user_id(value)

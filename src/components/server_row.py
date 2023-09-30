from gi.repository import Adw
from src.server import Server


class ServerRow(Adw.ActionRow):
    __gtype_name__ = "MarmaladeServerRow"

    server: Server

    def __init__(self, server: Server, **kwargs) -> None:
        super().__init__(**kwargs)
        self.server = server
        self.set_selectable(True)
        self.set_icon("go-next-symbolic")
        self.update_from_server()

    def update_from_server(self) -> None:
        self.set_title(self.server.name)
        self.set_subtitle(self.server.address)

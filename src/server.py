from gi.repository import GObject


class Server(GObject.Object):
    """Class representing a Jellyfin server"""

    __name: str

    @GObject.Property(type=str)
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    __address: str

    @GObject.Property(type=str)
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, value: str) -> None:
        self.__address = value

    def __init__(self, name: str, address: str) -> None:
        self.__name = name
        self.__address = address

    def asdict(self) -> dict:
        return {
            "name": self.__name,
            "address": self.__address,
        }

    def __str__(self) -> str:
        return f"Server (name: {self.__name}, address: {self.__address})"

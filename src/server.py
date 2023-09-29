class Server:
    """Class representing a Jellyfin server"""

    name: str
    address: str

    def __init__(self, name: str, address: str) -> None:
        self.name = name
        self.address = address

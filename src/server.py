from typing import NamedTuple


class Server(NamedTuple):
    """Class representing a Jellyfin server"""

    name: str
    address: str

from typing import NamedTuple


class Server(NamedTuple):
    """Class representing a Jellyfin server"""

    name: str
    address: str
    server_id: str

    def __eq__(self, other: "Server") -> bool:
        if not isinstance(other, Server):
            return False
        return (self.address == other.address) and (self.server_id == other.server_id)

    def __hash__(self) -> int:
        return hash((self.address, self.server_id))

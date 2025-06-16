from typing import NamedTuple


class ServerInfo(NamedTuple):
    """Class representing a Jellyfin server"""

    name: str
    address: str
    server_id: str

    def __eq__(self, other: "ServerInfo") -> bool:
        if not isinstance(other, ServerInfo):
            return False
        return self.address == other.address

    def __hash__(self) -> int:
        return hash(self.address)
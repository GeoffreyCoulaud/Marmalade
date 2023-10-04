from typing import NamedTuple


class Server(NamedTuple):
    """Class representing a Jellyfin server"""

    name: str
    address: str
    # TODO add sever_id (use with address for __eq__)

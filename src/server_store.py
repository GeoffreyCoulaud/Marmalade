from src.reactive_set import ReactiveSet
from src.server import Server
from src.store import FileStore


class ServerStore(
    FileStore,
    ReactiveSet[Server],
):
    """Set containing, saving and loading servers"""

    def to_simple(self):
        return [server._asdict() for server in self]

    def update_from_simple(self, simple):
        # Ensured to get latest format
        servers = [Server(**server_dict) for server_dict in simple]
        self.update(servers)

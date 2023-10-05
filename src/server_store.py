from src.reactive_set import ReactiveSet
from src.server import Server
from src.store import FileStore, Migrator


class ServerStoreMigrator(Migrator):
    """Class in charge of server store file format migration"""

    migrators = {}


class ServerStore(
    FileStore,
    ReactiveSet[Server],
):
    """Set containing, saving and loading servers"""

    migrator: ServerStoreMigrator

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.migrator = ServerStoreMigrator()

    def to_simple(self):
        return {
            "meta": {
                "format_version": 1,
            },
            "content": [server._asdict() for server in self],
        }

    def update_from_simple(self, simple):
        # Ensured to get latest format
        content = simple["content"]
        servers = [Server(**server_dict) for server_dict in content]
        self.update(servers)

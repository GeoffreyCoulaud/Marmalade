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

    def dump_to_json_compatible(self):
        # A change in this format must be accompanied by a migration method
        return {
            "meta": {
                "format_version": 1,
            },
            "content": [server._asdict() for server in self],
        }

    def load_from_json_compatible(self, json_compatible_data):
        # Ensured to get latest format
        content = json_compatible_data["content"]
        servers = [Server(**server_dict) for server_dict in content]
        self.update(servers)

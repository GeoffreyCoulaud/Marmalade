from src.reactive_set import ReactiveSet
from src.server import Server
from src.store import FileStore


class ServerStore(
    FileStore[list[dict[str, str]]],
    ReactiveSet[Server],
):
    """Set containing, saving and loading servers"""

    def dump_to_json_compatible(self):
        return [server._asdict() for server in self]

    def load_from_json_compatible(self, json_compatible_data):
        servers = (Server(**server_dict) for server_dict in json_compatible_data)
        self.update(servers)

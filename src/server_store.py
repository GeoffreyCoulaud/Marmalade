import json
import logging

from src.reactive_set import ReactiveSet
from src.server import Server
from src.store import FileStore


class ServerStore(FileStore, ReactiveSet):
    """Set containing, saving and loading servers"""

    def save(self) -> None:
        """Save servers to disk"""
        servers_dicts = [server._asdict() for server in self]
        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump(servers_dicts, file, indent=4)
        except OSError as error:
            logging.error("Couldn't save servers to disk", exc_info=error)

    def load(self) -> None:
        """Load servers from disk"""
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                server_dicts = json.load(file)
        except FileNotFoundError:
            self.file_path.touch()
            logging.info("Created servers file")
        except (OSError, json.JSONDecodeError) as error:
            logging.error("Couldn't load servers from disk", exc_info=error)
        else:
            servers = (Server(**server_dict) for server_dict in server_dicts)
            self.update(servers)

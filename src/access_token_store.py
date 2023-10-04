from src.bookmarked_collections import BookmarkedDefaultDict, BookmarkedSet
from src.server import Server
from src.store import FileStore, Migrator


class AccessTokenStoreMigrator(Migrator):
    """Class in charge of access token store file format migration"""

    migrators = {}


class AccessTokenStore(
    FileStore,
    BookmarkedDefaultDict[Server, BookmarkedSet[str]],
):
    """Class in charge of keeping track of the server access tokens"""

    migrator: AccessTokenStoreMigrator

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.default_factory = BookmarkedSet
        self.migrator = AccessTokenStoreMigrator()

    def add_token(self, server: Server, token: str):
        self[server].add(token)

    def dump_to_json_compatible(self):
        return {
            "meta": {
                "format_version": 1,
            },
            "content": [
                (server, list(tokens_set)) for server, tokens_set in self.items()
            ],
        }

    def load_from_json_compatible(self, json_compatible_data):
        content = json_compatible_data["content"]
        for server, tokens_list in content:
            for token in tokens_list:
                self.add_token(server, token)

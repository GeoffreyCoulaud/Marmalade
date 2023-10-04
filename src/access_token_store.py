from src.bookmarked_collections import BookmarkedDefaultDict, BookmarkedSet
from src.server import Server
from src.store import FileStore


class AccessTokenStore(
    FileStore[list[tuple[Server, list[str]]]],
    BookmarkedDefaultDict[Server, BookmarkedSet[str]],
):
    """Class in charge of keeping track of the server access tokens"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.default_factory = BookmarkedSet

    def add_token(self, server: Server, token: str):
        self[server].add(token)

    def dump_to_json_compatible(self):
        return [(server, list(tokens_set)) for server, tokens_set in self.items()]

    def load_from_json_compatible(self, json_compatible_data):
        for server, tokens_list in json_compatible_data:
            for token in tokens_list:
                self.add_token(server, token)

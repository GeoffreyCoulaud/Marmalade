from src.bookmarked_collections import BookmarkedBidict, BookmarkedDefaultDict
from src.server import Server
from src.store import FileStore


class AccessTokenStore(
    FileStore,
    BookmarkedDefaultDict[Server, BookmarkedBidict[str, str]],
):
    """Class in charge of keeping track of the server access tokens"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.default_factory = BookmarkedBidict

    def add_token(self, server: Server, user_id: str, token: str):
        self[server][user_id] = token

    def to_simple(self):
        return {
            "bookmark": self._bookmark,
            "content": [
                (server._asdict(), tokens_bidict.to_simple())
                for server, tokens_bidict in self.items()
            ],
        }

    def update_from_simple(self, simple):
        content = simple["content"]
        for server_dict, simple_bidict in content:
            server = Server(**server_dict)
            userid_tokens_map = BookmarkedBidict.from_simple(simple_bidict)
            self[server].update(userid_tokens_map)
        bookmark = simple["bookmark"]
        self.set_bookmark(bookmark)

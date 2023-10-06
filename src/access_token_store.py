from src.bookmarked_collections import BookmarkedBidict, BookmarkedDict
from src.server import Server
from src.store import FileStore


class AccessTokenStore(
    FileStore,
    BookmarkedDict[Server, BookmarkedBidict[str, str]],
):
    """Class in charge of keeping track of the server access tokens"""

    def add_token(self, server: Server, user_id: str, token: str):
        if server not in self:
            self[server] = BookmarkedBidict()
        self[server][user_id] = token

    def to_simple(self):
        return {
            "bookmark": self._bookmark._asdict(),
            "content": [
                (server._asdict(), tokens_bidict.to_simple())
                for server, tokens_bidict in self.items()
            ],
        }

    def update_from_simple(self, simple):
        content = simple["content"]
        for server_dict, simple_bidict in content:
            self[Server(**server_dict)] = BookmarkedBidict.from_simple(simple_bidict)
        bookmark = Server(**simple["bookmark"])
        self.set_bookmark(bookmark)

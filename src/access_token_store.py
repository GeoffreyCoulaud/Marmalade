from src.bookmarked_collections import BookmarkedDefaultDict, BookmarkedSet
from src.server import Server
from src.store import FileStore


class AccessTokenStore(FileStore, BookmarkedDefaultDict[Server, BookmarkedSet[str]]):
    """Class in charge of keeping track of the server access tokens"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.default_factory = BookmarkedSet

    def add_token(self, server: Server, token: str):
        self[server].add(token)

    def load(self):
        print("Loading access tokens from disk isn't implemented")
        # TODO implement loading access tokens

    def save(self):
        print("Saving acces stokens to disk isn't implemented")
        # TODO implement saving access tokens

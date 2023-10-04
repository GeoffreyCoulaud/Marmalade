from abc import ABC, abstractmethod
from collections import defaultdict
from typing import Collection, Generic, TypeVar

from src.server import Server
from src.store import FileStore

_UNSET = object()
_KT = TypeVar("_KT")
_VT = TypeVar("_VT")


class AbstractBookmarked(Generic[_KT, _VT]):
    """Abstract bookmarked class"""

    _bookmark: _UNSET | _KT = _UNSET

    def set_bookmark(self, key: _KT):
        self._bookmark = key

    def unset_bookmark(self) -> None:
        self._bookmark = _UNSET

    @abstractmethod
    def get_bookmark(self) -> _VT:
        pass


class BookmarkedSubscriptable(ABC, AbstractBookmarked[_KT, _VT]):
    """Mixin for subscriptable types to give them a bookmark"""

    def get_bookmark(self) -> _VT:
        return self[self._bookmark]


class BookmarkedDict(dict[_KT, _VT], BookmarkedSubscriptable[_KT, _VT]):
    """A dict with a bookmark on a key"""


class BookmarkedDefaultDict(defaultdict[_KT, _VT], BookmarkedSubscriptable[_KT, _VT]):
    """A default dict with a bookmark on a key"""

    def get_bookmark(self) -> _VT:
        if self._bookmark is _UNSET:
            return KeyError("Unset bookmark")
        return super().get_bookmark()


class BookmarkedCollection(ABC, Collection[_VT], AbstractBookmarked[_VT, _VT]):
    """Mixin for collections to give them a bookmark on a value"""

    def get_bookmark(self) -> _VT:
        if self._bookmark is _UNSET:
            raise KeyError("Unset bookmark")
        return self._bookmark


class BookmarkedSet(set[_VT], BookmarkedCollection[_VT, _VT]):
    """A set with a bookmark on a value"""


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

from abc import ABC, abstractmethod
from collections import defaultdict
from typing import Collection, Generic, TypeVar

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")


class AbcBookmarked(Generic[_KT, _VT]):
    """Abstract bookmarked class"""

    # HACK: use a different sentinel when PEP 661 is accepted.
    # This means that even if None would be a valid bookmark, it wouldn't be accepted.
    # However, using None as a bookmark would be discouraged anyway.
    _bookmark: None | _KT = None

    def set_bookmark(self, key: _KT):
        self._bookmark = key

    def unset_bookmark(self) -> None:
        self._bookmark = None

    @abstractmethod
    def get_bookmark(self) -> _VT:
        pass


class BookmarkedSubscriptableMixin(ABC, AbcBookmarked[_KT, _VT]):
    """Mixin for subscriptable types to give them a bookmark"""

    @abstractmethod
    def __getitem__(self, key: _KT) -> _VT:
        pass

    def get_bookmark(self) -> _VT:
        if self._bookmark is None:
            raise KeyError("Unset bookmark")
        return self[self._bookmark]


class BookmarkedDict(dict[_KT, _VT], BookmarkedSubscriptableMixin[_KT, _VT]):
    """A dict with a bookmark on a key"""


class BookmarkedDefaultDict(
    defaultdict[_KT, _VT], BookmarkedSubscriptableMixin[_KT, _VT]
):
    """A default dict with a bookmark on a key"""

    def get_bookmark(self) -> _VT:
        if self._bookmark is None:
            raise KeyError("Unset bookmark")
        return super().get_bookmark()


class BookmarkedCollectionMixin(ABC, Collection[_VT], AbcBookmarked[_VT, _VT]):
    """Mixin for collections to give them a bookmark on a value"""

    def get_bookmark(self) -> _VT:
        if self._bookmark is None:
            raise KeyError("Unset bookmark")
        return self._bookmark


class BookmarkedSet(set[_VT], BookmarkedCollectionMixin[_VT]):
    """A set with a bookmark on a value"""

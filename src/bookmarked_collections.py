from abc import ABC, abstractmethod
from collections import defaultdict
from typing import Collection, Generic, TypeVar

_UNSET = object()
_KT = TypeVar("_KT")
_VT = TypeVar("_VT")


class AbcBookmarked(Generic[_KT, _VT]):
    """Abstract bookmarked class"""

    _bookmark: _UNSET | _KT = _UNSET

    def set_bookmark(self, key: _KT):
        self._bookmark = key

    def unset_bookmark(self) -> None:
        self._bookmark = _UNSET

    @abstractmethod
    def get_bookmark(self) -> _VT:
        pass


class BookmarkedSubscriptableMixin(ABC, AbcBookmarked[_KT, _VT]):
    """Mixin for subscriptable types to give them a bookmark"""

    def get_bookmark(self) -> _VT:
        return self[self._bookmark]


class BookmarkedDict(dict[_KT, _VT], BookmarkedSubscriptableMixin[_KT, _VT]):
    """A dict with a bookmark on a key"""


class BookmarkedDefaultDict(
    defaultdict[_KT, _VT], BookmarkedSubscriptableMixin[_KT, _VT]
):
    """A default dict with a bookmark on a key"""

    def get_bookmark(self) -> _VT:
        if self._bookmark is _UNSET:
            return KeyError("Unset bookmark")
        return super().get_bookmark()


class BookmarkedCollectionMixin(ABC, Collection[_VT], AbcBookmarked[_VT, _VT]):
    """Mixin for collections to give them a bookmark on a value"""

    def get_bookmark(self) -> _VT:
        if self._bookmark is _UNSET:
            raise KeyError("Unset bookmark")
        return self._bookmark


class BookmarkedSet(set[_VT], BookmarkedCollectionMixin[_VT, _VT]):
    """A set with a bookmark on a value"""

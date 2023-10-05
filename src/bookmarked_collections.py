from abc import abstractmethod
from collections import defaultdict
from typing import Any, Collection, Generic, TypeVar

from bidict import bidict

from src.simple import Simple

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")


class AbcBookmarked(Simple, Generic[_KT, _VT]):
    """Abstract bookmarked class"""

    _bookmark: None | _KT = None

    def set_bookmark(self, bookmark: _KT):
        """
        Set the bookmarked identifier.

        Note that None can never be a valid bookmark as it is a sentinel value.
        See PEP 661 for details on the sentinels proposal.
        """
        self._bookmark = bookmark

    def unset_bookmark(self) -> None:
        """Unset the bookmark"""
        self._bookmark = None

    @abstractmethod
    def get_bookmark(self) -> _VT:
        """Get the bookmarked value"""

    @abstractmethod
    def _check_bookmark(self) -> None:
        """
        Check that the bookmarked value is valid.

        Raises a KeyError if it's invalid.
        Does nothing if it's valid.
        """


class BookmarkedSubscriptable(AbcBookmarked[_KT, _VT]):
    """
    Mixin for subscriptable types to give them a bookmark.

    Supported subscriptable types are:
    - Mappings
    - Sequences
    """

    @abstractmethod
    def __getitem__(self, key: _KT) -> _VT:
        pass

    def _check_bookmark(self) -> None:
        if self._bookmark is None:
            raise KeyError("Unset bookmark")
        if self._bookmark not in self:
            raise KeyError("Bookmark key not present")

    def get_bookmark(self) -> _VT:
        self._check_bookmark()
        return self[self._bookmark]

    def get_bookmark_key(self) -> _KT:
        """Get the bookmarked mapping key"""
        self._check_bookmark()
        return self._bookmark


class BookmarkedDict(
    dict[_KT, _VT],
    BookmarkedSubscriptable[_KT, _VT],
):
    """A dict with a bookmark on a key"""

    def to_simple(self) -> Any:
        return {
            "bookmark": self._bookmark,
            "content": dict(self),
        }

    @classmethod
    def from_simple(cls, simple):
        instance = cls(simple["content"])
        instance.set_bookmark(simple["bookmark"])
        return instance


class BookmarkedDefaultDict(
    defaultdict[_KT, _VT],
    BookmarkedDict[_KT, _VT],
):
    """A default dict with a bookmark on a key"""


class BookmarkedBidict(
    bidict[_KT, _VT],
    BookmarkedDict[_KT, _VT],
):
    """A bidirectional dict (unique keys AND values) with a bookmark on a key"""


class BookmarkedCollection(
    Collection[_VT],
    AbcBookmarked[_VT, _VT],
):
    """Mixin for collections to give them a bookmark on a value"""

    def _check_bookmark(self):
        if self._bookmark is None:
            raise KeyError("Unset bookmark")

    def set_bookmark(self, bookmark: _KT):  # pylint: disable=useless-parent-delegation
        """Set a bookmark on a contained value"""
        return super().set_bookmark(bookmark)

    def get_bookmark(self) -> _VT:
        self._check_bookmark()
        return self._bookmark

    def to_simple(self) -> Any:
        return {
            "bookmark": self._bookmark,
            "content": list(self),
        }

    @classmethod
    def from_simple(cls, simple):
        instance = cls(simple["content"])
        instance.set_bookmark(simple["bookmark"])
        return instance


class BookmarkedSet(
    set[_VT],
    BookmarkedCollection[_VT],
):
    """A set with a bookmark on a value"""

from abc import ABC, abstractmethod
from typing import Any


class Simple(ABC):
    """
    An interface for objects that can be converted to and created from a
    JSON-compatible object.

    Note that in the case of a Collection, the caller is in charge of making sure
    that its contents are JSON-compatible, to_simple will not change the contents.
    This is the case because to_simple doesn't keep the original class information.
    """

    @abstractmethod
    def to_simple(self) -> Any:
        """Convert the instance to a JSON-compatible object"""

    @abstractmethod
    def update_from_simple(self, simple: Any) -> None:
        """Update the instance from a JSON-compatible object"""

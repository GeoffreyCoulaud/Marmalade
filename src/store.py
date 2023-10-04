from abc import ABC, abstractmethod
from pathlib import Path


class BaseStore(ABC):
    """
    Base Store class

    A store is in charge of saving and loading its data
    """

    @abstractmethod
    def save(self) -> None:
        """Save the store items to file"""

    @abstractmethod
    def load(self) -> None:
        """Load store items from disk"""


class FileStore(BaseStore):
    """Base store class saving its data to a file"""

    file_path: Path

    def __init__(self, *args, file_path: Path, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.file_path = file_path

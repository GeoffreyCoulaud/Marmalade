import json
import logging
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Generic, TypeVar

JsonReprT = TypeVar("JsonReprT")


class BaseStore(ABC, Generic[JsonReprT]):
    """
    Base Store class

    A store is in charge of saving and loading its data
    """

    @property
    def _class_name(self) -> str:
        return self.__class__.__name__

    @abstractmethod
    def dump_to_json_compatible(self) -> JsonReprT:
        """Get a JSON-compatible representation of the contents"""

    @abstractmethod
    def load_from_json_compatible(self, json_compatible_data: JsonReprT) -> None:
        """Load contents from a JSON-compatible representation"""

    @abstractmethod
    def save(self) -> None:
        """Save the store items to file"""

    @abstractmethod
    def load(self) -> None:
        """Load store items from disk"""


class FileStore(BaseStore[JsonReprT]):
    """Base store class saving its data to a file"""

    file_path: Path

    def __init__(self, *args, file_path: Path, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.file_path = file_path

    def save(self) -> None:
        """Save servers to disk"""
        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                json_compatible = self.dump_to_json_compatible()
                json.dump(json_compatible, file, indent=4)

        except OSError as error:
            logging.error(
                "Couldn't save %s contents to file",
                self._class_name,
                exc_info=error,
            )

    def load(self) -> None:
        """Load servers from disk"""
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data: JsonReprT = json.load(file)

        except FileNotFoundError:
            self.file_path.touch()
            self.save()
            logging.info("Created %s store file", self._class_name)

        except (OSError, json.JSONDecodeError) as error:
            logging.error(
                "Couldn't load %s contents from file",
                self._class_name,
                exc_info=error,
            )

        else:
            self.load_from_json_compatible(data)

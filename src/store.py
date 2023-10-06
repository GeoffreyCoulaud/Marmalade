import json
import logging
from abc import abstractmethod
from pathlib import Path

from src.simple import Simple


class BaseStore(Simple):
    """
    Base Store class

    A store is in charge of saving and loading its data
    """

    @property
    def _class_name(self) -> str:
        return self.__class__.__name__

    @abstractmethod
    def save(self) -> None:
        """Save the store items to file"""

    @abstractmethod
    def _load(self) -> None:
        """Load store items from disk"""


class FileStore(BaseStore):
    """Base store class saving its data to a file"""

    file_path: Path

    def __init__(self, *args, file_path: Path, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.file_path = file_path
        self._load()

    def save(self) -> None:
        """Save store items to disk"""
        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                simple = self.to_simple()
                json.dump(simple, file, indent=4)

        except OSError as error:
            logging.error(
                "Couldn't save %s contents to file",
                self._class_name,
                exc_info=error,
            )

    def _create_file(self) -> None:
        self.file_path.touch()
        self.save()
        logging.info("Created %s store file", self._class_name)

    def _load(self) -> "FileStore":
        """
        Load servers from disk.

        Migrates to the latest json compatible format.
        Data loss may occur if the format are incompatible.
        """

        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

        except FileNotFoundError:
            self._create_file()
            return

        except (OSError, json.JSONDecodeError) as error:
            logging.error(
                "Couldn't load %s contents from file",
                self._class_name,
                exc_info=error,
            )
            return

        # Load from json compatibe format
        self.update_from_simple(data)

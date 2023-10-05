import json
import logging
from abc import abstractmethod
from pathlib import Path
from typing import Any, Callable, Optional

from src.simple import Simple


class Migrator:
    """
    Class in charge of dict format migration.

    The migrators property is a (source_version -> migration_method) mapping.
    Migration methods return a migrated object with an updated format version.
    Migration methods must not create lower versions, else an infinite loop will happen.
    """

    migrators: dict[int, Callable] = {}

    def migrate(self, start_obj: dict[str, Any]) -> dict[str, Any]:
        obj = start_obj
        while True:
            try:
                version = obj["meta"]["format_version"]
            except (TypeError, KeyError) as error:
                raise ValueError("Can't migrate object without a version") from error
            if version not in self.migrators:
                # No more migration to do
                break
            # Migrate
            obj = self.migrators[version](obj)
        return obj


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
    migrator: Optional[Migrator] = None

    def __init__(self, *args, file_path: Path, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.file_path = file_path
        self._load()

    def save(self) -> None:
        """Save servers to disk"""
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

        # Migrate data
        if self.migrator is not None:
            data = self.migrator.migrate(data)

        # Load from json compatibe format
        self.update_from_simple(data)

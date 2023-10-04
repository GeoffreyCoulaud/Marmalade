import json
import logging
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Callable, Optional


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


class BaseStore(ABC):
    """
    Base Store class

    A store is in charge of saving and loading its data
    """

    @property
    def _class_name(self) -> str:
        return self.__class__.__name__

    @abstractmethod
    def dump_to_json_compatible(self) -> Any:
        """Get a JSON-compatible representation of the contents"""

    @abstractmethod
    def load_from_json_compatible(self, json_compatible_data: Any) -> None:
        """Load contents from a JSON-compatible representation"""

    @abstractmethod
    def save(self) -> None:
        """Save the store items to file"""

    @abstractmethod
    def load(self) -> None:
        """Load store items from disk"""


class FileStore(BaseStore):
    """Base store class saving its data to a file"""

    file_path: Path
    migrator: Optional[Migrator] = None

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
        """
        Load servers from disk.

        Migrates to the latest json compatible format.
        Data loss may occur if the format are incompatible.
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

        except FileNotFoundError:
            self.file_path.touch()
            self.save()
            logging.info("Created %s store file", self._class_name)
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
        self.load_from_json_compatible(data)

import logging
from contextlib import closing
from pathlib import Path
from sqlite3 import Connection, OperationalError, connect
from typing import Sequence


class CorruptedDatabase(Exception):
    """Error raised when trying to read a broken database"""


class CustomDatabase(object):

    __database_file: Path

    def __init__(self, *args, database_file: Path, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__database_file = database_file
        self.apply_migrations()

    def get_connection(self) -> closing[Connection]:
        """
        Get a database connection.

        Should be used in a with statement.
        Will be closed automatically, but not commit.
        Enforces thread-locality.
        """
        return closing(connect(str(self.__database_file), check_same_thread=True))

    def execute_blind(self, *query_param_tuples: tuple[str, dict | Sequence]) -> None:
        """Execute queries then commit to the database. Doesn't return a result"""
        with self.get_connection() as db:
            for query, params in query_param_tuples:
                db.execute(query, params)
            db.commit()

    def get_database_version(self) -> str:
        """Get the database version string"""
        with self.get_connection() as db:
            try:
                query = "SELECT row_value FROM Meta WHERE row_key = 'version'"
                cursor = db.execute(query)
            except OperationalError:
                # No table 'meta', database is freshly created
                return "v0"
            row = cursor.fetchone()
            if row is None:
                # No meta value with key 'version', invalid
                raise CorruptedDatabase("Database has no 'version' key in meta table")
            # Return version from database
            return row[0]

    def apply_migrations(self):
        """Migrate the database schema to the latest version"""

        # Get migration scripts
        scripts = {}
        migrations_dir = Path(__file__).parent / "migrations"
        for path in migrations_dir.glob("v*.sql"):
            source_version, _rest = path.name.split("_", 1)
            scripts[source_version] = path

        # Apply migrations
        with self.get_connection() as db:
            while True:
                source_version = self.get_database_version()
                logging.debug("Database at version %s", source_version)
                # No new migration
                if not source_version in scripts.keys():
                    break
                # Get the next migration script
                # (remove it from the local map to avoid errors creating infinite loops)
                script_path = scripts[source_version]
                del scripts[source_version]
                with open(script_path, "r", encoding="utf-8") as file:
                    script = file.read()
                # Apply the migration
                logging.debug('Applying migration script "%s"', script_path.stem)
                db.executescript(script)
        logging.debug("Database migration finished")

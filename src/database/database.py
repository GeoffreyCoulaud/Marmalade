import logging
from contextlib import closing
from pathlib import Path
from sqlite3 import Connection, OperationalError, Row, connect
from typing import Any, MutableMapping, NamedTuple, Optional, Sequence

from src.reactive_set import ReactiveSet
from src.server import Server


class CorruptedDatabase(Exception):
    """Error raised when trying to read a broken database"""


class ActiveTokenInfo(NamedTuple):
    """Object describing the active token"""

    server: Server
    token: str


class DataHandler(object):
    """
    Settings interface class on top a sqlite database file.

    - Exposes a `server` ReactiveSet that is mirrored in the database
    """

    servers: ReactiveSet[Server]

    __db_file: Path
    __server_added_handler_id: int
    __server_removed_handler_id: int

    def __init__(self, *args, file: Path, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__db_file = file
        self.__apply_migrations()

        # fmt: off
        self.servers = ReactiveSet()
        self.__server_added_handler_id = self.servers.emitter.connect("item-added", self.__on_server_added)
        self.__server_removed_handler_id = self.servers.emitter.connect("item-removed", self.__on_server_removed)
        self.__load_servers()
        # fmt: on

    def connect(self) -> Connection:
        """
        Get a database connection.

        Should be used in a with statement.
        Will be closed automatically, but not commit.
        Enforces thread-locality.
        """
        return closing(connect(str(self.__db_file), check_same_thread=True))

    def __execute_blind(self, *query_param_tuples: tuple[str, dict | Sequence]) -> None:
        """Execute queries then commit to the database. Doesn't return a result"""
        with self.connect() as db:
            for query, params in query_param_tuples:
                db.execute(query, params)
            db.commit()

    def get_database_version(self) -> str:
        """Get the database version string"""
        with self.connect() as db:
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

    def __apply_migrations(self):
        """Migrate the database schema to the latest version"""

        # Get migration scripts
        scripts = {}
        migrations_dir = Path(__file__).parent / "migrations"
        for path in migrations_dir.glob("v*.sql"):
            source_version, _rest = path.name.split("_", 1)
            scripts[source_version] = path

        # Apply migrations
        with self.connect() as db:
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

    def __load_servers(self) -> None:
        """
        Load the servers from the database into the servers set.
        Inhibit server added handler for the time of this method.
        """
        with (
            self.servers.emitter.handler_block(self.__server_added_handler_id),
            self.connect() as db,
        ):
            cursor = db.execute("SELECT name, address, server_id FROM Servers")
            cursor.row_factory = lambda _cursor, row: Server(*row)
            for server in cursor:
                self.servers.add(server)

    def __on_server_added(self, _emitter, server: Server) -> None:
        """
        React to a server being added.
        Replicates the change into the database.
        """
        query = "INSERT INTO Servers (address, name, server_id) VALUES (?, ?, ?)"
        params = (server.address, server.name, server.server_id)
        self.__execute_blind((query, params))
        logging.debug("Saved server to db: %s", server)

    def __on_server_removed(self, _emitter, server: Server) -> None:
        """
        React to a server being removed.
        Replicates the change into the database.
        """
        del_tokens_query = ("DELETE FROM Tokens WHERE address = ?", (server.address,))
        del_server_query = ("DELETE FROM Servers WHERE address = ?", (server.address,))
        self.__execute_blind(del_tokens_query, del_server_query)
        logging.debug("Deleted server from db: %s", server)

    def add_active_token(self, address: str, user_id: str, token: str) -> None:
        """Add a token and set it as active"""
        query = """
            INSERT INTO Tokens (address, user_id, token, active) 
            VALUES (?, ?, ?, 1)
        """
        params = (address, user_id, token)
        self.__execute_blind((query, params))
        logging.debug("Logged in user_id %s on %s", user_id, address)

    def set_active_token(self, address: str, user_id: str) -> None:
        """Set the app's active token"""
        query = "UPDATE Tokens SET active = 1 WHERE address = ? AND user_id = ?"
        params = (address, user_id)
        self.__execute_blind((query, params))

    def unset_active_token(self) -> None:
        """Deactivate the active token"""
        query = "UPDATE Tokens SET active = 0 WHERE active = 1"
        params = ()
        self.__execute_blind((query, params))

    def get_active_token(self) -> Optional[ActiveTokenInfo]:
        """
        Get the token that is currently logged on.

        If there is no active token, returns None
        Else, returns (server, user_id, token)

        - When logging into a server, the token is active
        - When logging off, the token is kept and set not active
        - When logging out, the token is removed
        """
        query = """
            SELECT s.name, s.address, s.server_id, t.token 
            FROM Servers AS s
            INNER JOIN Tokens AS t
            WHERE t.active = 1
        """
        with self.connect() as db:
            cursor = db.execute(query)
            row: None | tuple = cursor.fetchone()
            if row is None:
                return row
            name, address, server_id, token = row
            server = Server(name=name, address=address, server_id=server_id)
            return ActiveTokenInfo(server=server, token=token)

    def remove_token(self, address: str, user_id: str):
        """Remove the server access token for the given user_id"""
        query = "DELETE FROM Tokens WHERE address = ? AND user_id = ?"
        params = (address, user_id)
        self.__execute_blind((query, params))
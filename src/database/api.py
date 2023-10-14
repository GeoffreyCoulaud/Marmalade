import logging
from contextlib import closing
from pathlib import Path
from sqlite3 import Connection, OperationalError, connect
from typing import NamedTuple, Optional, Sequence


class CorruptedDatabase(Exception):
    """Error raised when trying to read a broken database"""


class ServerInfo(NamedTuple):
    """Class representing a Jellyfin server"""

    name: str
    address: str
    server_id: str

    def __eq__(self, other: "ServerInfo") -> bool:
        if not isinstance(other, ServerInfo):
            return False
        return self.address == other.address

    def __hash__(self) -> int:
        return hash(self.address)


class UserInfo(NamedTuple):
    """Object describing a user"""

    user_id: str
    name: str

    def __eq__(self, other: "UserInfo") -> bool:
        if not isinstance(other, UserInfo):
            return False
        return self.user_id == other.user_id

    def __hash__(self) -> int:
        return hash(self.user_id)


class TokenInfo(NamedTuple):
    """Object describing a token"""

    device_id: str
    token: str


class ActiveTokenInfo(NamedTuple):
    """Object describing the active token"""

    address: str
    user_id: str
    token_info: TokenInfo


class DataHandler(object):
    """
    Settings interface class on top a sqlite database file.
    """

    __db_file: Path

    def __init__(self, *args, file: Path, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__db_file = file
        self.__apply_migrations()

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

    def get_servers(self) -> list[ServerInfo]:
        query = """
            SELECT name, address, server_id 
            FROM Servers
            ORDER BY connected_timestamp DESC, created_timestamp DESC
        """
        servers = []
        with self.connect() as db:
            cursor = db.execute(query)
            cursor.row_factory = lambda _cursor, row: ServerInfo(*row)
            for server in cursor:
                servers.append(server)
        return servers

    def add_server(self, server: ServerInfo) -> None:
        """Add a server to the database"""
        query = "INSERT INTO Servers (address, name, server_id) VALUES (?, ?, ?)"
        params = (server.address, server.name, server.server_id)
        self.__execute_blind((query, params))
        logging.debug("Saved server to db: %s", server)

    def remove_server(self, address: str) -> None:
        """Remove a server by address from the database"""
        query = "DELETE FROM Servers WHERE address = ?"
        args = (address,)
        self.__execute_blind((query, args))
        logging.debug("Deleted server with address %s from db", address)

    def update_connected_timestamp(self, address: str) -> None:
        """Update a server's connected timestamp"""
        query = """
            UPDATE Servers 
            SET connected_timestamp = CURRENT_TIMESTAMP 
            WHERE address = ?;
        """
        args = (address,)
        self.__execute_blind((query, args))
        logging.debug("Updated %s connected timestamp", address)

    def add_token(self, address: str, user_id: str, token: str, device_id: str) -> None:
        """Add a token to the database"""
        query = """
            INSERT OR REPLACE INTO Tokens (address, user_id, device_id, token) 
            VALUES (?, ?, ?, ?)
        """
        params = (address, user_id, device_id, token)
        self.__execute_blind((query, params))

    def get_token(self, address: str, user_id: str) -> Optional[TokenInfo]:
        """Get the saved authentication token for a user id on a server"""
        query = """
            SELECT device_id, token 
            FROM Tokens 
            WHERE address = ? AND user_id = ?
        """
        params = (address, user_id)
        with self.connect() as db:
            row: None | tuple[str, str] = db.execute(query, params).fetchone()
        if row is None:
            return None
        device_id, token = row
        return TokenInfo(device_id=device_id, token=token)

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

        - When logging into a server, the token is active
        - When logging off, the token is kept and set not active
        - When logging out, the token is removed
        """
        query = """
            SELECT s.address, t.user_id, t.device_id, t.token
            FROM Servers AS s
            INNER JOIN Tokens AS t
            ON t.address = s.address
            WHERE t.active = 1
        """
        with self.connect() as db:
            cursor = db.execute(query)
            row: None | tuple = cursor.fetchone()
            if row is None:
                return row
            address, user_id, device_id, token = row
            return ActiveTokenInfo(
                address=address,
                user_id=user_id,
                token_info=TokenInfo(
                    device_id=device_id,
                    token=token,
                ),
            )

    def remove_token(self, address: str, user_id: str):
        """Remove the server access token for the given user_id"""
        query = "DELETE FROM Tokens WHERE address = ? AND user_id = ?"
        params = (address, user_id)
        self.__execute_blind((query, params))

    def add_users(self, address: str, *users: UserInfo) -> None:
        query = """
            INSERT OR REPLACE
            INTO Users (address, user_id, name)
            VALUES (?, ?, ?)
        """
        row_values = [(address, user.user_id, user.name) for user in users]
        with self.connect() as db:
            db.executemany(query, row_values)
            db.commit()

    def get_user(self, address: str, user_id: str) -> Optional[UserInfo]:
        """Get user info for an address and user id"""
        query = """SELECT name FROM Users WHERE address = ? AND user_id = ?"""
        params = (address, user_id)
        with self.connect() as db:
            row = db.execute(query, params).fetchone()
        if row is None:
            return None
        return UserInfo(user_id=user_id, name=row[0])

    def get_authenticated_users(self, address: str) -> list[UserInfo]:
        """Get a set of authenticated user_id for a server address"""
        query = """
            SELECT u.user_id, u.name
            FROM Tokens AS t
            INNER JOIN Users AS u ON t.address = u.address AND t.user_id = u.user_id
            INNER JOIN Servers AS s ON s.address = t.address
            WHERE s.address = ?
        """
        params = (address,)
        with self.connect() as db:
            cursor = db.execute(query, params)
            rows = cursor.fetchall()
        user_infos = [UserInfo(user_id=uid, name=name) for uid, name in rows]
        return user_infos

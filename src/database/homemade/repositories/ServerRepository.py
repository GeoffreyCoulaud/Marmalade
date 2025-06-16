import logging

from src.database.homemade.CustomDatabase import CustomDatabase
from src.database.homemade.models.ServerInfo import ServerInfo


class ServerRepository(object):

    __database: CustomDatabase

    def __init__(self, database: CustomDatabase) -> None:
        self.__database = database

    def get_servers(self) -> list[ServerInfo]:
        query = """
            SELECT name, address, server_id 
            FROM Servers
            ORDER BY connected_timestamp DESC, created_timestamp DESC
        """
        servers = []
        with self.__database.get_connection() as db:
            cursor = db.execute(query)
            cursor.row_factory = lambda _cursor, row: ServerInfo(*row)
            for server in cursor:
                servers.append(server)
        return servers

    def add_server(self, server: ServerInfo) -> None:
        """Add a server to the database"""
        query = "INSERT INTO Servers (address, name, server_id) VALUES (?, ?, ?)"
        params = (server.address, server.name, server.server_id)
        self.__database.execute_blind((query, params))
        logging.debug("Saved server to db: %s", server)

    def remove_server(self, address: str) -> None:
        """Remove a server by address from the database"""
        query = "DELETE FROM Servers WHERE address = ?"
        args = (address,)
        self.__database.execute_blind((query, args))
        logging.debug("Deleted server with address %s from db", address)

    def update_server_connected_timestamp(self, address: str) -> None:
        """Update a server's connected timestamp"""
        query = """
            UPDATE Servers 
            SET connected_timestamp = CURRENT_TIMESTAMP 
            WHERE address = ?;
        """
        args = (address,)
        self.__database.execute_blind((query, args))
        logging.debug("Updated %s connected timestamp", address)

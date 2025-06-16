"""
TODO: Migrate all that to SQLAlchemy + Alembic

Tables are : Servers, Users, Tokens, Meta

Meta is just a key-value store for the database version
Meta's known keys should be stored in an enum here.
Known keys are:
- version: the database version string

Servers table is for storing server info
The address column is unique

Users table is for storing user info on a server
The user_id column is unique for a server

Tokens table is for storing access tokens belonging to a user on a server, plus a device id
Tokens table also has an 'active' column to store the currently active token.
A user should have only one token on a server.

The database should use UUIDs for all table primary keys.

With an ORM, to avoid N+1 we should get user and server when getting tokens.
However since we're using SQLite, efficiency is not really a concern.
We can use autoconnet instead of manual database connection management too.
"""

from pathlib import Path

from src.database.homemade.models.ServerInfo import ServerInfo
from src.database.homemade.models.TokenInfo import ActiveTokenInfo, TokenInfo
from src.database.homemade.models.UserInfo import UserInfo
from src.database.homemade.repositories.ServerRepository import ServerRepository
from src.database.homemade.repositories.TokenRepository import TokenRepository
from src.database.homemade.repositories.UserRepository import UserRepository


class EverythingRepository(object):
    """
    Settings interface class on top a sqlite database file.
    Will be removed after the split in multiple repositories.
    """

    __db_file: Path

    __server_repository: ServerRepository
    __token_repository: TokenRepository
    __user_repository: UserRepository

    def __init__(
        self,
        server_repository: ServerRepository,
        token_repository: TokenRepository,
        user_repository: UserRepository,
    ) -> None:
        self.__server_repository = server_repository
        self.__token_repository = token_repository
        self.__user_repository = user_repository

    def get_servers(self) -> list[ServerInfo]:
        return self.__server_repository.get_servers()

    def add_server(self, server: ServerInfo) -> None:
        return self.__server_repository.add_server(server)

    def remove_server(self, address: str) -> None:
        return self.__server_repository.remove_server(address)

    def update_server_connected_timestamp(self, address: str) -> None:
        return self.__server_repository.update_server_connected_timestamp(address)

    def add_token(self, address: str, user_id: str, token: str, device_id: str) -> None:
        return self.__token_repository.add_token(address, user_id, token, device_id)

    def get_token(self, address: str, user_id: str) -> None | TokenInfo:
        return self.__token_repository.get_token(address, user_id)

    def set_active_token(self, address: str, user_id: str) -> None:
        return self.__token_repository.set_active_token(address, user_id)

    def unset_active_token(self) -> None:
        return self.__token_repository.unset_active_token()

    def get_active_token(self) -> None | ActiveTokenInfo:
        return self.__token_repository.get_active_token()

    def remove_token(self, address: str, user_id: str):
        return self.__token_repository.remove_token(address, user_id)

    def add_users(self, address: str, *users: UserInfo) -> None:
        return self.__user_repository.add_users(address, *users)

    def get_user(self, address: str, user_id: str) -> None | UserInfo:
        return self.__user_repository.get_user(address, user_id)

    def get_authenticated_users(self, address: str) -> list[UserInfo]:
        return self.__user_repository.get_authenticated_users(address)

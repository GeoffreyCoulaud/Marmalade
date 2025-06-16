from src.database.homemade.CustomDatabase import CustomDatabase
from src.database.homemade.models.UserInfo import UserInfo


class UserRepository(object):
    """Repository for managing users"""

    __database: CustomDatabase

    def __init__(self, database: CustomDatabase) -> None:
        self.__database = database

    def add_users(self, address: str, *users: UserInfo) -> None:
        query = """
            INSERT OR REPLACE
            INTO Users (address, user_id, name)
            VALUES (?, ?, ?)
        """
        row_values = [(address, user.user_id, user.name) for user in users]
        with self.__database.get_connection() as db:
            db.executemany(query, row_values)
            db.commit()

    def get_user(self, address: str, user_id: str) -> None | UserInfo:
        """Get user info for an address and user id"""
        query = """SELECT name FROM Users WHERE address = ? AND user_id = ?"""
        params = (address, user_id)
        with self.__database.get_connection() as db:
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
        with self.__database.get_connection() as db:
            cursor = db.execute(query, params)
            rows = cursor.fetchall()
        user_infos = [UserInfo(user_id=uid, name=name) for uid, name in rows]
        return user_infos

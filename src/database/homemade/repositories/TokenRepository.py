from src.database.homemade.CustomDatabase import CustomDatabase
from src.database.homemade.models.TokenInfo import ActiveTokenInfo, TokenInfo


class TokenRepository(object):
    """Repository for managing tokens"""

    __database: CustomDatabase

    def __init__(self, database: CustomDatabase) -> None:
        self.__database = database

    def add_token(self, address: str, user_id: str, token: str, device_id: str) -> None:
        """Add a token to the database"""
        query = """
            INSERT OR REPLACE INTO Tokens (address, user_id, device_id, token) 
            VALUES (?, ?, ?, ?)
        """
        params = (address, user_id, device_id, token)
        self.__database.execute_blind((query, params))

    def get_token(self, address: str, user_id: str) -> None | TokenInfo:
        """Get the saved authentication token for a user id on a server"""
        query = """
            SELECT device_id, token 
            FROM Tokens 
            WHERE address = ? AND user_id = ?
        """
        params = (address, user_id)
        with self.__database.get_connection() as db:
            row: None | tuple[str, str] = db.execute(query, params).fetchone()
        if row is None:
            return None
        device_id, token = row
        return TokenInfo(device_id=device_id, token=token)

    def set_active_token(self, address: str, user_id: str) -> None:
        """Set the app's active token"""
        query = "UPDATE Tokens SET active = 1 WHERE address = ? AND user_id = ?"
        params = (address, user_id)
        self.__database.execute_blind((query, params))

    def unset_active_token(self) -> None:
        """Deactivate the active token"""
        query = "UPDATE Tokens SET active = 0 WHERE active = 1"
        params = ()
        self.__database.execute_blind((query, params))

    def get_active_token(self) -> None | ActiveTokenInfo:
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
        with self.__database.get_connection() as db:
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
        self.__database.execute_blind((query, params))

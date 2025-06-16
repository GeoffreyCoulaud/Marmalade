from typing import NamedTuple


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
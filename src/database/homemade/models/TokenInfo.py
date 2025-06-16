from typing import NamedTuple


class TokenInfo(NamedTuple):
    """Object describing a token"""

    device_id: str
    token: str


class ActiveTokenInfo(NamedTuple):
    """Object describing the active token"""

    address: str
    user_id: str
    token_info: TokenInfo

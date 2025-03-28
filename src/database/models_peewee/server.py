from peewee import TextField, TimestampField, UUIDField

from src.database.base_model import BaseModel


class Server(BaseModel):
    """Entity containing Jellyfin server information"""

    id_ = UUIDField(
        primary_key=True,
        help_text="Internal ID, used to make joins",
    )

    address = TextField(unique=True)
    name = TextField(help_text="Name reported by the server in its public info")
    jellyfin_id = TextField(help_text="ID reported by the server in its public info")
    created_timestamp = TimestampField()

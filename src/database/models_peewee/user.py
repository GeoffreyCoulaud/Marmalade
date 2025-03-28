from peewee import SQL, ForeignKeyField, TextField, UUIDField

from src.database.base_model import BaseModel
from src.database.server import Server


class User(BaseModel):

    class Meta:
        constraints = [
            # Jellyfin user IDs are unique per server
            SQL("UNIQUE (jellyfin_id, server_id)"),
        ]

    id_ = UUIDField(
        primary_key=True,
        help_text="Internal ID, used to make joins",
    )

    server = ForeignKeyField(Server, backref="users", object_id_name="server_id")
    jellyfin_id = TextField()
    name = TextField()

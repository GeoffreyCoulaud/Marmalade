from http import server
from textwrap import dedent

from peewee import SQL, BooleanField, ForeignKeyField, TextField, UUIDField

from src.database.base_model import BaseModel
from src.database.user import User


class AuthentificationToken(BaseModel):

    class Meta:
        constraints = [
            # A user has maximum one token
            SQL("UNIQUE (user_id)"),
        ]

    id_ = UUIDField(
        primary_key=True,
        help_text="Internal ID, used to make joins",
    )

    user = ForeignKeyField(User, backref="tokens", object_id_name="user_id")
    token = TextField()
    device_id = TextField(
        # fmt: off
        help_text=dedent("""
            Note: you can only have a single access token per device id
            See https://github.com/home-assistant/core/issues/70124#issuecomment-1278033166
        """)
        # fmt: on
    )
    active = BooleanField(
        null=True,
        unique=True,
        # fmt: off
        help_text=dedent("""
            Shorthand to get the last active token
            Nulls don't count as duplicates, so you can have multiple inactive tokens
        """)
        # fmt: on
    )

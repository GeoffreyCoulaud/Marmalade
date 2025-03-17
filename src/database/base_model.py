from peewee import Model

import shared


class BaseModel(Model):
    """
    Base entity model class

    Database connections are created on the fly, since we're local-only using SQLite
    """

    class Meta:
        database = shared.database
        legacy_table_names = False

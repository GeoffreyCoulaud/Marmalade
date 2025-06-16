from typing import List

from sqlalchemy import TIMESTAMP, UUID, Column, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.orm.base_model import Base
from src.database.orm.user import User


class Server(Base):
    """Entity containing Jellyfin server information"""

    __tablename__ = "server"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    created_timestamp = Column(TIMESTAMP)
    address: Mapped[str] = mapped_column(Text, unique=True)
    # Name reported by the server in its public info
    name: Mapped[str] = mapped_column(Text)
    # ID reported by the server in its public info
    jellyfin_id: Mapped[str] = mapped_column(Text)

    users: Mapped[List["User"]] = relationship(
        back_populates="server", cascade="all, delete-orphan"
    )

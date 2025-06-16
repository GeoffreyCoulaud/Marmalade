from sqlalchemy import UUID, ForeignKey, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models_sqlalchemy.base_model import Base
from src.database.models_sqlalchemy.server import Server
from src.database.models_sqlalchemy.token import AuthenticationToken


class User(Base):
    __tablename__ = "user"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    jellyfin_id: Mapped[str] = mapped_column(Text)
    name: Mapped[str] = mapped_column(Text)

    server_id: Mapped[UUID] = mapped_column(ForeignKey("server.id"))
    server: Mapped["Server"] = relationship(back_populates="users")
    tokens: Mapped["AuthenticationToken | None"] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    __table_args__ = (UniqueConstraint("jellyfin_id", "server_id"),)

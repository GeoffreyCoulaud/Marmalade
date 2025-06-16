from sqlalchemy import Boolean, ForeignKey, Text, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.orm.base_model import Base


class AuthenticationToken(Base):
    __tablename__ = "authentication_token"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    token: Mapped[str] = mapped_column(Text)
    # Note: you can only have a single access token per device id
    device_id: Mapped[str] = mapped_column(Text)
    # Shorthand to get the last active token.
    # Nulls don't count as duplicates
    active: Mapped[bool | None] = mapped_column(Boolean, unique=True)

    # Relationship is one to one, only one token per user
    user_id = mapped_column(ForeignKey("user.id"))
    user = relationship(back_populates="tokens", single_parent=True)

    __table_args__ = (UniqueConstraint("user_id"),)

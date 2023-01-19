from sqlalchemy import (
    Column, String
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import composite
import uuid

from app.infrastructure.db.sqlalchemy.models import Base

from app.core.user import entities
from app.core.user.entities import value_objects as vo


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    _email = Column("email", String, nullable=False)
    _username = Column("username", String, nullable=False)
    _hashed_password = Column("hashed_password", String, nullable=False)

    email = composite(vo.Email, _email)
    username = composite(vo.UserName, _username)
    hashed_password = composite(vo.HashedPassword, _hashed_password)


def user_mapping(mapper_registry):
    table = User.__table__
    mapper_registry.map_imperatively(
        entities.User, table,
    )



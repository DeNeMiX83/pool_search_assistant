from sqlalchemy import Column, ForeignKey, BigInteger, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.infrastructure.db.sqlalchemy.models import Base
from app.core.pool import entities


class LikePool(Base):
    __tablename__ = "like_pools"
    __table_args__ = (UniqueConstraint("user_id", "pool_id"),)

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )
    pool_id = Column(
        BigInteger, ForeignKey("pools.id", ondelete="CASCADE"),
        nullable=False,
    )

    user = relationship(
        "app.infrastructure.db.sqlalchemy.models.user.user.User",
    )
    pool = relationship(
        "app.infrastructure.db.sqlalchemy.models.pool.pool.Pool",
    )


def like_pools_mapping(mapper_registry):
    table = LikePool.__table__
    mapper_registry.map_imperatively(
        entities.PoolLike, table,
    )

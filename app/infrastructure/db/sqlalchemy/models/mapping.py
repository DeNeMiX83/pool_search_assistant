from app.infrastructure.db.sqlalchemy.models import (
    pool_mapping, user_mapping, like_pools_mapping,
)
from app.infrastructure.db.sqlalchemy.models.base import Base


def start_mappers():
    mapper_registry = Base.registry
    like_pools_mapping(mapper_registry)
    pool_mapping(mapper_registry)
    user_mapping(mapper_registry)

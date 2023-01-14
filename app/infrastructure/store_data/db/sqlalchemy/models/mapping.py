from app.infrastructure.store_data.db.sqlalchemy.models.pool.pool import pool_mapping
from app.infrastructure.store_data.db.sqlalchemy.models.base import Base

def start_mappers():
    mapper_registry = Base.registry
    pool_mapping(mapper_registry)
    # address_mapping(mapper_registry)
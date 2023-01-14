from sqlalchemy import (
    Column, String, Boolean
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import composite
import uuid

from app.infrastructure.store_data.db.sqlalchemy.models.base import Base

from app.core.pool.entities.pool import PoolEntity
from app.core.pool.entities.value_objects.address import LocationValueObject
from app.core.pool.entities.value_objects.contacts import ContactsValueObject

print(Base.metadata.tables)
class Pool(Base):
    __tablename__ = 'pools'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    email = Column(String, nullable=False)
    web_site = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)

    administrative_area = Column(String, nullable=False)
    district = Column(String, nullable=False)
    address = Column(String, nullable=False)

    name = Column(String, nullable=False)
    has_equipment_rental = Column(Boolean, nullable=False)
    has_tech_service = Column(Boolean, nullable=False)
    has_dressing_room = Column(Boolean, nullable=False)
    has_eatery = Column(Boolean, nullable=False)
    has_toilets = Column(Boolean, nullable=False)
    has_wifi = Column(Boolean, nullable=False)
    has_cash_machine = Column(Boolean, nullable=False)
    has_first_aid_post = Column(Boolean, nullable=False)
    has_music = Column(Boolean, nullable=False)
    is_paid = Column(Boolean, nullable=False)
    how_suitable_for_disabled = Column(String, nullable=False)



def pool_mapping(mapper_registry):
    mapper_registry.map_imperatively(
        PoolEntity, Pool,
        properties={
            "location": composite(
                LocationValueObject,
                Pool.administrative_area,
                Pool.district,
                Pool.address,
            ),
            "contacts": composite(
                ContactsValueObject,
                Pool.email,
                Pool.web_site,
                Pool.phone_number,
            ),
        }
    )
    
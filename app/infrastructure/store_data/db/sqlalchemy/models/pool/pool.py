from sqlalchemy import (
    Column, String, Boolean
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import composite
import uuid

from app.infrastructure.store_data.db.sqlalchemy.models import Base

from app.core.pool import entities
from app.core.pool.entities import value_objects as vo

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
    table = Pool.__table__
    mapper_registry.map_imperatively(
        entities.Pool, table,
        properties={
            "location": composite(
                vo.Location,
                table.c.administrative_area,
                table.c.district,
                table.c.address,
            ),
            "contacts": composite(
                vo.Contacts,
                table.c.email,
                table.c.web_site,
                table.c.phone_number,
            ),
        }
    )
    
from sqlalchemy import (
    Column, String, Boolean, BigInteger
)
from sqlalchemy.orm import composite

from app.infrastructure.store_data.db.sqlalchemy.models import Base

from app.core.pool import entities
from app.core.pool.entities import value_objects as vo

class Pool(Base):
    __tablename__ = 'pools'

    id = Column('id', BigInteger, primary_key=True)

    email = Column('email', String, nullable=False)
    web_site = Column('web_site', String, nullable=False)
    phone_number = Column('phone_number', String, nullable=False)

    administrative_area = Column('administrative_area', String, nullable=False)
    district = Column('district', String, nullable=False)
    address = Column('address', String, nullable=False)

    name = Column('name', String, nullable=False)
    has_equipment_rental = Column('has_equipment_rental', Boolean, nullable=False)
    has_tech_service = Column('has_tech_service', Boolean, nullable=False)
    has_dressing_room = Column('has_dressing_room', Boolean, nullable=False)
    has_eatery = Column('has_eatery', Boolean, nullable=False)
    has_toilets = Column('has_toilets', Boolean, nullable=False)
    has_wifi = Column('has_wifi', Boolean, nullable=False)
    has_cash_machine = Column('has_cash_machine', Boolean, nullable=False)
    has_first_aid_post = Column('has_first_aid_post', Boolean, nullable=False)
    has_music = Column('has_music', Boolean, nullable=False)
    is_paid = Column('is_paid', Boolean, nullable=False)
    how_suitable_for_disabled = Column('how_suitable_for_disabled', String, nullable=False)


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
    
from sqlalchemy import Column, String, Boolean, BigInteger
from sqlalchemy.orm import composite

from app.infrastructure.db.sqlalchemy.models import Base

from app.core.pool import entities
from app.core.pool.entities import value_objects as vo


class Pool(Base):
    __tablename__ = "pools"

    id = Column("id", BigInteger, primary_key=True)

    email = Column("email", String)
    web_site = Column("web_site", String)
    phone_number = Column("phone_number", String)

    administrative_area = Column("administrative_area", String, nullable=False)
    district = Column("district", String, nullable=False)
    address = Column("address", String, nullable=False)

    name = Column("name", String)
    has_equipment_rental = Column("has_equipment_rental", Boolean)
    has_tech_service = Column("has_tech_service", Boolean)
    has_dressing_room = Column("has_dressing_room", Boolean)
    has_eatery = Column("has_eatery", Boolean)
    has_toilets = Column("has_toilets", Boolean)
    has_wifi = Column("has_wifi", Boolean)
    has_cash_machine = Column("has_cash_machine", Boolean)
    has_first_aid_post = Column("has_first_aid_post", Boolean)
    has_music = Column("has_music", Boolean)
    is_paid = Column("is_paid", Boolean)
    how_suitable_for_disabled = Column("how_suitable_for_disabled", String)


def pool_mapping(mapper_registry):
    table = Pool.__table__
    mapper_registry.map_imperatively(
        entities.Pool,
        table,
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
        },
    )

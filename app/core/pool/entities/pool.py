from dataclasses import dataclass
from app.core.shared.entities.entity import Entity
from app.core.pool.entities.value_objects.address import LocationValueObject
from app.core.pool.entities.value_objects.contacts import ContactsValueObject


@dataclass()
class PoolEntity(Entity):
    name: str
    location: LocationValueObject 
    contacts: ContactsValueObject
    has_equipment_rental: bool
    has_tech_service: bool
    has_dressing_room: bool
    has_eatery: bool
    has_toilets: bool
    has_wifi: bool
    has_cash_machine: bool
    has_first_aid_post: bool
    has_music: bool
    is_paid: bool
    how_suitable_for_disabled: str
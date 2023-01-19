from dataclasses import dataclass
from dataclasses import field
from app.core.shared.entities.entity import Entity
from app.core.pool.entities.value_objects.location import Location
from app.core.pool.entities.value_objects.contacts import Contacts


@dataclass()
class Pool(Entity):
    id: int = field(init=False, default=None)
    name: str
    location: Location 
    contacts: Contacts
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
from dataclasses import dataclass
from app.core.shared.entities.entity import Entity
from uuid import UUID


@dataclass()
class AddressEntity(Entity):
    pool_id: UUID
    administrative_area: str
    district: str
    address: str
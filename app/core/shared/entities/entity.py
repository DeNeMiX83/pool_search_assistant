from dataclasses import dataclass
from .value_objects.uuid import UUID 
import uuid

@dataclass()
class Entity():
    id: UUID

    @classmethod
    def generate_id(cls) -> UUID:
        return uuid.uuid4()
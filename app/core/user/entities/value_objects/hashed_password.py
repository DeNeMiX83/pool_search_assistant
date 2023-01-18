from dataclasses import dataclass
from app.core.shared.entities.value_objects.value_object import ValueObject


@dataclass(frozen=True)
class HashedPassword(ValueObject, str):
    value: str
from dataclasses import dataclass
from app.core.shared.entities.value_object import ValueObject


@dataclass()
class LocationValueObject(ValueObject):
    administrative_area: str
    district: str
    address: str

    def __composite_values__(self):
        return (
            self.administrative_area,
            self.district,
            self.address,
        )
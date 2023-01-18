from dataclasses import dataclass
from app.core.shared.entities.value_objects.value_object import ValueObject


@dataclass()
class Contacts(ValueObject):
    email: str
    web_site: str
    phone_number: str

    def __composite_values__(self):
        return (
            self.email,
            self.web_site,
            self.phone_number,
        )
from dataclasses import dataclass
from app.core.shared.entities.value_objects.value_object import ValueObject


@dataclass(frozen=True)
class RawPassword(ValueObject):
    value: str

    def __post_init__(self):
        v = self.value

        if not isinstance(v, str):
            raise TypeError("Password must be a string")

        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")

        if len(v) > 32:
            raise ValueError("Password must be at most 32 characters long")

        if not any(char.isdigit() for char in v):
            raise ValueError("Password must contain at least one digit")

        if not any(char.isupper() for char in v):
            raise ValueError(
                "Password must contain at least one uppercase letter"
            )

        if not any(char.islower() for char in v):
            raise ValueError(
                "Password must contain at least one lowercase letter"
            )

        if not any(char in "!@#$%^&*()_+" for char in v):
            raise ValueError(
                "Password must contain at least one special character"
            )

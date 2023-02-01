from app.core.shared.entities.entity import Entity
from app.core.user.entities import value_objects as vo
from dataclasses import dataclass


@dataclass
class User(Entity):
    email: vo.Email
    username: vo.UserName
    hashed_password: vo.HashedPassword

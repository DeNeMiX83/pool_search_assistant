from dataclasses import dataclass
from app.core.shared.entities.entity import Entity
from app.core.shared.entities import value_objects as vo


@dataclass()
class PoolLike(Entity):
    user_id: vo.UUID
    pool_id: int

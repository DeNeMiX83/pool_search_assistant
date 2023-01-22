from app.shared.dto import BaseDto
from app.core.shared.entities import value_objects as vo


class PoolCreate(BaseDto):
    email: str
    web_site: str
    phone_number: str

    administrative_area: str
    district: str
    address: str

    name: str
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


class PoolLike(BaseDto):
    user_id: vo.UUID
    pool_id: int


class PoolUnlike(PoolLike):
    id: vo.UUID

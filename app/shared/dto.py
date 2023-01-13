from pydantic import BaseModel


class Dto(BaseModel):
    id: str = None

    class Config:
        orm_mode = True
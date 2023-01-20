from pydantic import BaseModel


class BaseDto(BaseModel):
    class Config:
        orm_mode = True


class WriteDto(BaseDto):
    pass


class ReadDto(BaseDto):
    id: str = None

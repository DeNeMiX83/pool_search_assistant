from pydantic import BaseModel


class WriteDto(BaseModel):

    class Config:
        orm_mode = True


class ReadDto(WriteDto):
    id: str = None

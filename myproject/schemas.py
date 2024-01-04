from pydantic import BaseModel


class user_base(BaseModel):
    fullName: str
    userName: str
    password: str


class user(user_base):
    id: int

    class Config:
        orm_mode = True


class user_create(user_base):
    pass

from pydantic import BaseModel
from typing import Optional
from bcrypt import hashpw, gensalt


class user_base(BaseModel):
    fullName: str
    userName: str
    password: str


class user(user_base):
    id: int

    class Config:
        orm_mode = True


class user_create(user_base):
    def hash_password(self):
        # Hash the password using bcrypt
        self.password = hashpw(self.password.encode('utf-8'), gensalt())
    pass


class user_update(BaseModel):
    fullName: Optional[str] = None
    userName: Optional[str] = None
    password: Optional[str] = None


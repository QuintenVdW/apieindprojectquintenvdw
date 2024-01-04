from sqlalchemy import Column, Integer, String

from database import Base


class user(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    fullName = Column(String, index=True)
    userName = Column(String, unique=True, index=True)
    password = Column(String)

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from oauth2 import get_current_user

import crud
import models
import schemas
from database import SessionLocal, engine
import os

if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

# "sqlite:///./sqlitedb/sqlitedata.db"
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/getUser/", response_model=schemas.user)
def read_user(name: str, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_name=name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.delete("/deleteUser/", response_model=schemas.user)
def read_user(name: str, db: Session = Depends(get_db)):
    db_user = crud.delete_user_by_name(db, user_name=name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/createUser/", response_model=schemas.user)
def create_user(user: schemas.user_create, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_name=user.userName)
    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")

    user.hash_password()

    return crud.create_user(db=db, user=user)


@app.put("/updateUser/", response_model=schemas.user)
def update_user(user_id: int, user_update: schemas.user_update, db: Session = Depends(get_db)):
    updated_user = crud.update_user(db, user_id, user_update)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

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


@app.get("/faction/Jedi", response_model=list[schemas.Star_wars])
def read_users(limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_faction(db, faction=2, limit=limit)
    return users


@app.get("/faction/Sith", response_model=list[schemas.Star_wars])
def read_users(limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_faction(db, faction=1, limit=limit)
    return users


@app.get("/character/", response_model=schemas.Star_wars)
def read_user(name: str, db: Session = Depends(get_db)):
    db_user = crud.get_name(db, user_name=name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.delete("/character/", response_model=schemas.Star_wars)
def read_user(name: str, db: Session = Depends(get_db)):
    db_user = crud.delete_character_by_name(db, user_name=name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/characters_add/", response_model=schemas.Star_wars)
def create_user(user: schemas.Star_wars_create, db: Session = Depends(get_db)):
    db_user = crud.get_name(db, user_name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Name already registered")
    return crud.create_character(db=db, user=user)


@app.post("/faction_add/", response_model=schemas.Faction)
def create_faction(faction: schemas.FactionCreate, db: Session = Depends(get_db)):
    faction_check = crud.get_faction_by_name(db, faction_name=faction.name)
    if faction_check:
        raise HTTPException(status_code=400, detail="Name already registered")
    return crud.create_faction(db=db, faction=faction)


from sqlalchemy.orm import Session

import models
import schemas


def get_name(db: Session, user_name: str):
    return db.query(models.Star_wars).filter(models.Star_wars.name == user_name).first()


def delete_character_by_name(db: Session, user_name: str):
    db_user = db.query(models.Star_wars).filter(models.Star_wars.name == user_name).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user
    return None


def get_faction_by_name(db: Session, faction_name: str):
    return db.query(models.Faction).filter(models.Faction.name == faction_name).first()


def get_faction(db: Session, faction: int, limit: int = 10):
    return db.query(models.Star_wars).filter(models.Star_wars.faction_id == faction).limit(limit).all()


def create_character(db: Session, user: schemas.Star_wars_create):
    db_star_Wars = models.Star_wars(**user.dict())
    db.add(db_star_Wars)
    db.commit()
    db.refresh(db_star_Wars)
    return db_star_Wars


def create_faction(db: Session, faction: schemas.FactionCreate):
    db_faction = models.Faction(**faction.dict())
    db.add(db_faction)
    db.commit()
    db.refresh(db_faction)
    return db_faction


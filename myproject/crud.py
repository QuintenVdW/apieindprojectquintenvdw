from sqlalchemy.orm import Session

import models
import schemas


def get_user(db: Session, user_name: str):
    return db.query(models.user).filter(models.user.name == user_name).first()


def delete_user_by_name(db: Session, user_name: str):
    db_user = db.query(models.user).filter(models.user.name == user_name).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user
    return None


def create_user(db: Session, user: schemas.user_create):
    db_star_Wars = models.user(**user.dict())
    db.add(db_star_Wars)
    db.commit()
    db.refresh(db_star_Wars)
    return db_star_Wars




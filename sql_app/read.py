from sqlalchemy.orm import Session

from . import models, schemas

def get_spots(db: Session, skip: int = 0):
    return db.query(models.Spots).offset(skip).all()

def get_zones(db: Session, skip: int = 0):
    return db.query(models.Zones).offset(skip).all()
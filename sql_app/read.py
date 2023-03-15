from sqlalchemy.orm import Session

from . import models, schemas

# FrontEnd Default View (Pins on the Map)
def get_spots(db: Session, skip: int = 0):
    return db.query(models.Spots).offset(skip).all()

def get_zones(db: Session, skip: int = 0):
    return db.query(models.Zones).offset(skip).all()

# FrontEnd Selected Pin on the Map
def get_zones_by_spot(db: Session, zoneGuid: str):
    return db.query(models.Zones).filter(models.Zones.zoneGuid == zoneGuid).all()
from sqlalchemy.orm import Session
from . import models

# Query single spot
def get_spot(db: Session, id: int):
    return db.query(models.Spot).filter(models.Spot.id == id).first()
# Query all spots
def get_spots(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Spot).offset(skip).limit(limit).all()
# Query all spots with daily rate
def get_prices(db: Session, skip: int = 0, limit: int = 100):
   return db.query(models.Spot.id, models.Spot.address, models.Zone.rate_daily).join(models.Zone).where(models.Spot.zone_guid == models.Zone.zone_guid).offset(skip).limit(limit).all()
    
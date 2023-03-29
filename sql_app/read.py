from sqlalchemy.orm import Session

from . import models, schemas

# Default View (Initial page load, green pins on the map)
def get_spots(db: Session, skip: int = 0):
    return db.query(models.Spots).offset(skip).all()

# IMPARK data Default View (red pins)
def get_impark_spots(db: Session, skip: int = 0):
    return db.query(models.Impark).offset(skip).all()

# Selected/Clicked Pin on the Map
def get_zones_by_spot(db: Session, zoneGuid: str):
    return db.query(models.Zones).filter(models.Zones.zoneGuid == zoneGuid).all()

# Dynamic Pricing
def get_prices_by_spot(db: Session, zoneGuid: str):
    return db.query(models.Spots.coveredParking, models.Spots.electricCharger, models.Spots.rating, models.Spots.reservedHours, models.Spots.spotCount, models.Zones.rateDaily, models.Zones.rateEvening, models.Zones.rateFull).join(models.Spots, models.Spots.zoneGuid == models.Zones.zoneGuid).filter(models.Zones.zoneGuid == zoneGuid).all()


# TESTING
def get_zones(db: Session, skip: int = 0):
    return db.query(models.Zones).offset(skip).all()
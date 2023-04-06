from sqlalchemy.orm import Session

from . import models, schemas

# Default View (Initial page load, green pins on the map)
def get_spots(db: Session, skip: int = 0):
    return db.query(models.Spots).offset(skip).all()

# IMPARK data Default View (red pins)
def get_impark_spots(db: Session, skip: int = 0):
    return db.query(models.Impark).offset(skip).all()

# Selected/Clicked Gryd Marker
def get_zones_by_spot(db: Session, zoneGuid: str):
    return db.query(models.Zones).filter(models.Zones.zoneGuid == zoneGuid).all()

# Selected/Clicked Impark Marker
def get_impark_details(db: Session, id: int):
    return db.query(models.Impark).filter(models.Impark.id == id).all()

# Dynamic Pricing
def get_prices_by_spot(db: Session, zoneGuid: str):
    return db.query(models.Spots.coveredParking, models.Spots.electricCharger, models.Spots.rating, models.Spots.reservedHours, models.Spots.spotCount, models.Zones.rateDaily, models.Zones.rateEvening, models.Zones.rateFull).join(models.Spots, models.Spots.zoneGuid == models.Zones.zoneGuid).filter(models.Zones.zoneGuid == zoneGuid).all()


# TESTING
def get_zones(db: Session, skip: int = 0):
    return db.query(models.Zones).offset(skip).all()

# FrontEnd Selected Pin on the Map
def get_zones_by_spot(db: Session, zoneGuid: str):
    return db.query(models.Zones).filter(models.Zones.zoneGuid == zoneGuid).all()

#Get Features from both tables for Dynamic Pricing 
def get_prices_by_spot(db: Session, zoneGuid: str):
    return db.query(models.Spots.latitude, models.Spots.longitude, models.Spots.coveredParking, models.Spots.electricCharger, models.Spots.rating, models.Spots.reservedHours, models.Spots.spotCount, models.Zones.rateDaily, models.Zones.rateEvening, models.Zones.rateFull).join(models.Spots, models.Spots.zoneGuid == models.Zones.zoneGuid).filter(models.Zones.zoneGuid == zoneGuid).all()

def get_prices_by_spot(db: Session, zoneGuid: str):
    return db.query(models.Spots.coveredParking, models.Spots.electricCharger, models.Spots.rating, models.Spots.reservedHours, models.Spots.spotCount, models.Zones.rateDaily, models.Zones.rateEvening, models.Zones.rateFull).join(models.Spots, models.Spots.zoneGuid == models.Zones.zoneGuid).filter(models.Zones.zoneGuid == zoneGuid).all()

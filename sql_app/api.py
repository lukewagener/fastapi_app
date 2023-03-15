from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import read, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/zones/", response_model=list[schemas.Zones])
def read_zones(skip: int = 0, db: Session = Depends(get_db)):
    zones = read.get_zones(db, skip=skip)
    return zones

# FrontEnd Default View (Pins on the Map)
@app.get("/spots/", response_model=list[schemas.Spots])
def read_spots(skip: int = 0, db: Session = Depends(get_db)):
    spots = read.get_spots(db, skip=skip)
    return spots

# FrontEnd Selected Pin on the Map
@app.get("/zones/{zoneGuid}", response_model=list[schemas.Zones])
def read_zone(zoneGuid: str, db: Session = Depends(get_db)):
    db_zone = read.get_zones_by_spot(db, zoneGuid=zoneGuid)
    return db_zone
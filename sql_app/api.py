from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import read, models, schemas
from .database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

from stub import get_data
from . import dynamic_pricing as dp

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Default View (Initial page load, green pins on the map)
@app.get("/spots", response_model=list[schemas.Spots])
async def read_spots(skip: int = 0, db: Session = Depends(get_db)):  
    spots = read.get_spots(db, skip=skip)
    return spots

# IMPARK data Default View (red pins)
@app.get("/impark", response_model=list[schemas.Impark])
def read_impark(db: Session = Depends(get_db)):  
    impark_data = read.get_impark_spots(db)
    return impark_data

# Selected/Clicked Gryd Marker
@app.get("/zones/{zoneGuid}", response_model=list[schemas.Zones])
def read_zone(zoneGuid: str, db: Session = Depends(get_db)):
    db_zone = read.get_zones_by_spot(db, zoneGuid=zoneGuid)
    return db_zone

# Selected/Clicked Impark Marker
@app.get("/impark/{id}", response_model=list[schemas.Impark])
def read_impark_details(id: int, db: Session = Depends(get_db)):
    impark_detail = read.get_impark_details(db, id=id)
    return impark_detail


# TESTING: running python function
@app.get("/test")
def super_test():
    test = get_data(3)
    return test

# TESTING: Zone table API
@app.get("/zones/", response_model=list[schemas.Zones])
def read_zones(skip: int = 0, db: Session = Depends(get_db)):
    zones = read.get_zones(db, skip=skip)
    return zones

# TESTING: DSML Team's function
#Dynamic pricing 
@app.get("/prices/{zoneGuid}", response_model=list[schemas.Dynamic])
def read_prices(zoneGuid: str, db: Session = Depends(get_db)):
    db_prices = read.get_prices_by_spot(db, zoneGuid=zoneGuid)
    return dp(db_prices)
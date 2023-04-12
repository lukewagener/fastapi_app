from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import json
from . import read, models, schemas
from .database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
from .dynamic_pricing import dynamic_pricing as dp

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


# GRYD data Default View (green pins)
@app.get("/spots", response_model=list[schemas.Spots])
async def read_spots(skip: int = 0, db: Session = Depends(get_db)):  
    spots = read.get_spots(db, skip=skip)
    return spots

# Selected/Clicked GRYD Marker
@app.get("/zones/{zoneGuid}", response_model=list[schemas.Zones])
def read_zone(zoneGuid: str, db: Session = Depends(get_db)):
    db_zone = read.get_zones_by_spot(db, zoneGuid=zoneGuid)
    return db_zone


# IMPARK data Default View (red pins)
@app.get("/impark", response_model=list[schemas.Impark])
def read_impark(db: Session = Depends(get_db)):  
    impark_data = read.get_impark_spots(db)
    return impark_data

# Selected/Clicked IMPARK Marker
@app.get("/impark/{id}", response_model=list[schemas.Impark])
def read_impark_details(id: int, db: Session = Depends(get_db)):
    impark_detail = read.get_impark_details(db, id=id)
    return impark_detail


# Dynamic Pricing (GRYD data)
@app.get("/prices/{zoneGuid}", response_model=list[schemas.Dynamic])
def read_prices(zoneGuid: str, db: Session = Depends(get_db)) -> dict:

    db_prices = read.get_prices_by_spot(db, zoneGuid=zoneGuid)
    print(db_prices)
    
    # convert json to python string
    str_prices = json.dumps(db_prices, default=str)
    # print(str_prices)

    # convert json to python dict
    dict_prices = json.loads(str_prices)
    # print(str_prices['latitude'])
    # print("dict", dict_prices)
    # dict_keys = list(dict_prices.keys())
    # print(dict_keys)
    # print(dict_prices)
    

    latitude = db_prices[0]['latitude']
    print(latitude)
    longitude = db_prices[0]['longitude']
    print(longitude)
    coveredParking = db_prices[0]['coveredParking']
    print(coveredParking)
    electricCharger = db_prices[0]['electricCharger']
    print(electricCharger)
    rating = db_prices[0]['rating']
    print(rating)
    reservedHours = db_prices[0]['reservedHours']
    print(reservedHours)
    spotCount = db_prices[0]['spotCount']
    print(spotCount)
    rateDaily = db_prices[0]['rateDaily']
    print(rateDaily)
    rateEvening = db_prices[0]['rateEvening']
    print(rateEvening)
    rateFull = db_prices[0]['rateFull']
    print(rateFull)
    commuter = db_prices[0]['commuter']
    print(commuter)
    eveningsWeekends = db_prices[0]['eveningsWeekends']
    print(eveningsWeekends)
    
    dict_prices = {
        'latitude': latitude,
        'longitude': longitude,
        'coveredParking': coveredParking,
        'electricCharger': electricCharger,
        'rating': rating,
        'reservedHours': reservedHours,
        'spotCount': spotCount,
        'rateDaily': rateDaily,
        'rateEvening': rateEvening,
        'rateFull': rateFull,
        'commuter': commuter,
        'eveningsWeekends': eveningsWeekends
    }
    print(dict_prices)
    print(list(dict_prices.keys()))
    print(list(dict_prices.values()))

    prices = dp(dict_prices)
    return prices
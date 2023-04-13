from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import read, models, schemas
from .database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
from .dynamic_pricing_revised import dynamic_pricing as dp
import json
from pydantic import BaseModel

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

# FrontEnd Default View (Pins on the Map)
@app.get("/spots/", response_model=list[schemas.Spots])
def read_spots(skip: int = 0, db: Session = Depends(get_db)):
    spots = read.get_spots(db, skip=skip)
    print(spots)
    return spots

# FrontEnd Selected Pin on the Map
@app.get("/zones/{zoneGuid}", response_model=list[schemas.Zones])
def read_zone(zoneGuid: str, db: Session = Depends(get_db)):
    db_zone = read.get_zones_by_spot(db, zoneGuid=zoneGuid)
    print(db_zone)
    return db_zone

class DynamicBase(BaseModel):
    rateHourly: float
    rateDaily: float
    rateWeekly: float
    rateMonthly: float
    Std_deviation: float

    class Config:
        allow_population_by_field_name = True

#Dynamic pricing 
@app.get("/prices/{zoneGuid}", response_model=list[DynamicBase])
def read_prices(zoneGuid: str, db: Session = Depends(get_db)) -> any:
    db_prices = read.get_prices_by_spot(db, zoneGuid=zoneGuid)

    # convert data to JSON string

    str_prices = json.dumps(db_prices, default=str)

    # convert json to python dict
    
    dict_prices = json.loads(str_prices)

    latitude = db_prices[0]['latitude']

    longitude = db_prices[0]['longitude']

    coveredParking = db_prices[0]['coveredParking']

    electricCharger = db_prices[0]['electricCharger']

    rating = db_prices[0]['rating']
   
    reservedHours = db_prices[0]['reservedHours']
  
    spotCount = db_prices[0]['spotCount']

    rateDaily = db_prices[0]['rateDaily']

    rateEvening = db_prices[0]['rateEvening']

    rateFull = db_prices[0]['rateFull']

    commuter = db_prices[0]['commuter']
 
    eveningsWeekends = db_prices[0]['eveningsWeekends']

    dict_prices = {
        'Latitude': latitude,
        'Longitude': longitude,
        'Covered_Parking': coveredParking,
        'Electric_charger': electricCharger,
        'Rating': rating,
        'Reserved_hours': reservedHours,
        'Spot_Count': spotCount,
        'Daily_Rate': rateDaily,
        'Evening_rate': rateEvening,
        'Full_Rate': rateFull,
        'Commuter': commuter,
        'eveningsWeekends': eveningsWeekends,
        'UtilizationByHours': 0,
        'Bus_Nearby': 0
    }

    prices = dp(dict_prices)
    print(prices)
    print("HOURLY", prices['hourly_price']),
    print("DAILY", prices['daily_price'])
   
    return [
        DynamicBase(rateHourly=prices['hourly_price'], rateDaily=prices['daily_price'], rateWeekly=prices['weekly_price'], rateMonthly=prices['monthly_price'], Std_deviation=prices['Std_deviation'])
    ]
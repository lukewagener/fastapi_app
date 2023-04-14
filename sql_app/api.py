from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import json
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
    print("DICT", dict_prices)
    latitude = db_prices[0][0]
    print(latitude)
    longitude = db_prices[0][1]

    coveredParking = db_prices[0][2]

    electricCharger = db_prices[0][3]

    rating = db_prices[0][4]
   
    reservedHours = db_prices[0][5]
  
    spotCount = db_prices[0][6]

    rateDaily = db_prices[0][7]

    rateEvening = db_prices[0][8]

    rateFull = db_prices[0][9]

    commuter = db_prices[0][10]
 
    eveningsWeekends = db_prices[0][11]

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
    print("DICT2", dict_prices)
    prices = dp(dict_prices)
    print(prices)
    print("HOURLY", prices['hourly_price']),
    print("DAILY", prices['daily_price'])
   
    return [
        DynamicBase(rateHourly=prices['hourly_price'], rateDaily=prices['daily_price'], rateWeekly=prices['weekly_price'], rateMonthly=prices['monthly_price'], Std_deviation=prices['Std_deviation'])
    ]
    
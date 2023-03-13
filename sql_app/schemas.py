from pydantic import BaseModel

class Properties(BaseModel):
    PropertyGuid: str
    ZoneGuid: str
    PropertyName: str
    ZoneGuid: str
    PropertyName: str
    ZoneName: str
    Address: str
    Postal code: str
    Latitude: float
    Longitude: float
    Covered Parking: bool
    Electric charger for EV: bool
    Block Heater: bool
    Rating: float
    ReservationCount: int
    ReservedHours: int
    SpotCount: int

    class Config:
        orm_mode = True

class Zones(BaseModel):
    PropertyName: str
    ZoneGuid: str
    ZoneName: str
    Hourly: float
    Daily rate: float
    Evening rate: int
    24/7: int
    Commuter: int
    Evenings & Weekends: int

    class Config:
        orm_mode = True
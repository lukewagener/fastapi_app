from pydantic import BaseModel

class PropertiesBase(BaseModel):
    zoneGuid: str
    propertyName: str
    zoneGuid: str
    propertyName: str
    zoneName: str
    address: str
    postalCode: str
    latitude: float
    longitude: float
    coveredParking: bool
    electricCharger: bool
    blockHeater: bool
    rating: float
    reservationCount: int
    reservedHours: int
    spotCount: int

class Properties(PropertiesBase):
    propertyGuid: str

    class Config:
        orm_mode = True

class ZonesBase(BaseModel):
    propertyName: str
    zoneName: str
    hourly: float
    dailyRate: float
    eveningRate: int
    fullRate: int
    commuter: int
    eveningsWeekends: int

class Zones(ZonesBase):
    zoneGuid: str

    class Config:
        orm_mode = True
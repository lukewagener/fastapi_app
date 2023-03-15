from pydantic import BaseModel

class SpotsBase(BaseModel):
    propertyGuid: str
    zoneGuid: str
    propertyName: str
    zoneName: str
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

class Spots(SpotsBase):
    class Config:
        orm_mode = True


class ZonesBase(BaseModel):
    zoneGuid: str
    propertyName: str
    zoneName: str
    rateHourly: float
    rateDaily: float
    rateEvening: int
    rateFull: int
    commuter: int
    eveningsWeekends: int

class Zones(ZonesBase):
    class Config:
        orm_mode = True
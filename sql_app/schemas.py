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

class ImparkBase(BaseModel):
    id: int
    address: str
    postalCode: str
    latitude: float
    longitude: float
    lowestMonthlyRate: float
    coveredParking: bool
    busNearby: bool
    distanceFromCenter: float
    usage: bool
    rangePointFive: float
    rangeOnePointZero: float
    rangeOnePointFive: float
    rangeTwoPointZero: float
    hourlyRate: float

class Impark(ImparkBase):
    class Config:
        orm_mode = True

class FeaturesBase(BaseModel):
    latitude: float
    longitude: float
    coveredParking: bool
    electricCharger: bool
    rating: int
    reservedHours: int
    spotCount: int
    rateDaily: float
    rateEvening: float
    rateFull: float
    commuter: int
    eveningsWeekends: int

class Features(FeaturesBase):
    class Config:
        orm_mode = True

class DynamicBase(BaseModel):
    rateHourly: float
    rateDaily: float
    rateEvening: float
    rateFull: float

class Dynamic(DynamicBase):
    class Config:
        orm_mode = True


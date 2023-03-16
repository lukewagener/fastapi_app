from pydantic import BaseModel

class SpotBase(BaseModel):
    address: str
    latitude: float
    longitude: float

class SpotCreate(SpotBase):
    pass

class Spot(SpotBase):
    postal: str
    property_guid: str
    zone_guid: str
    prop_name: str
    zone_name: str
    covered_park: bool
    ev_charger: bool
    block_heat: bool
    rating: int
    res_count: int
    res_hours: int
    spot_count: int
    
    class Config:
        orm_mode = True

class ZoneBase(BaseModel):
    zone_guid: str
    property_name: str
    zone_name: str

class ZoneCreate(ZoneBase):
    pass

class Zone(ZoneBase):
    rate_hourly: float
    rate_daily: float
    rate_evening: float
    rate_247: float
    commuter: int
    evenings_weekends: float

    class Config:
        orm_mode = True

# Schema for Joined table query
class SpotPriced(BaseModel):
    id: int
    address: str
    rate_daily: int

    class Config:
        orm_mode = True


# class SpotPricedBase(BaseModel):
#     postal: str
#     property_guid: str
#     zone_guid: str
#     prop_name: str
#     zone_name: str
#     covered_park: bool
#     ev_charger: bool
#     block_heat: bool
#     rating: int
#     res_count: int
#     res_hours: int
#     spot_count: int
#     zone_guid: str
#     property_name: str
#     commuter: int

# class SpotPriced(SpotPricedBase):
#     id: int
#     address: str
#     latitude: float
#     longitude: float
#     zone_name: str
#     rate_hourly: float
#     rate_daily: float
#     rate_evening: float
#     rate_247: float
#     evenings_weekends: float

#     class Config:
#         orm_mode = True

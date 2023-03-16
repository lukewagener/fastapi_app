from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Zone(Base):
    __tablename__ = "zones"

    zone_guid = Column(String, primary_key=True, index=True)
    property_name = Column(String)
    zone_name = Column(String)
    rate_hourly = Column(Integer)
    rate_daily = Column(Integer)
    rate_evening = Column(Integer)
    rate_247 = Column(Integer)
    commuter = Column(Integer)
    evenings_weekends = Column(Integer)

    spots = relationship("Spot", backref="zones", uselist=False)

class Spot(Base):
    __tablename__ = "spots"

    property_guid = Column(String, primary_key=True, index=True)
    zone_guid = Column(String, ForeignKey('zones.zone_guid'))
    prop_name = Column(String)
    zone_name = Column(String)
    address = Column(String)
    postal = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    covered_park = Column(Boolean)
    ev_charger = Column(Boolean)
    block_heat = Column(Boolean)
    rating = Column(Integer)
    res_count = Column(Integer)
    res_hours = Column(Integer)
    spot_count = Column(Integer)

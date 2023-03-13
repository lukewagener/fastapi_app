from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Properties(Base):
    __tablename__ = "properties"

    PropertyGuid = Column(String)
    ZoneGuid = Column("String", ForeignKey("zones.ZoneGuid"))
    PropertyName = Column(String)
    ZoneName = Column(String)
    Address = Column(String)
    Postal code = Column(String)
    Latitude = Column(Decimal)
    Longitude = Column(Decimal)
    Covered Parking = Column(Boolean)
    Electric charger for EV = Column(Boolean) 
    Block Heater = Column(Boolean)
    Rating = Column(Decimal)
    ReservationCount = Column(Integer)
    ReservedHours = Column(Integer)
    SpotCount = Column(Integer)


class Zones(Base):
    __tablename__ = "zones"

    PropertyName = Column(String)
    ZoneGuid = Column(String)
    ZoneName = Column(String)
    Hourly = Column(Decimal)
    Daily Rate = Column(Decimal)
    Evening Rate = Column(Integer)
    24/7 = Column(Integer)
    Commuter = Column(Integer)
    Evenings & Weekends = Column(Integer)
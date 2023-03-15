from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric
from sqlalchemy.orm import relationship

from .database import Base


class Spots(Base):
    __tablename__ = "spots"

    propertyGuid = Column(String, primary_key=True, index=True)
    zoneGuid = Column(String, ForeignKey('zones.zoneGuid'))
    propertyName = Column(String)
    zoneName = Column(String)
    address = Column(String)
    postalCode = Column(String)
    latitude = Column(Numeric)
    longitude = Column(Numeric)
    coveredParking = Column(Boolean)
    electricCharger = Column(Boolean) 
    blockHeater = Column(Boolean)
    rating = Column(Numeric)
    reservationCount = Column(Integer)
    reservedHours = Column(Integer)
    spotCount = Column(Integer)


class Zones(Base):
    __tablename__ = "zones"

    zoneGuid = Column(String, primary_key=True, index=True)
    propertyName = Column(String)
    zoneName = Column(String)
    rateHourly = Column(Numeric)
    rateDaily = Column(Numeric)
    rateEvening = Column(Integer)
    rateFull = Column(Integer)
    commuter = Column(Integer)
    eveningsWeekends = Column(Integer)

    spots = relationship("Spots", backref="zones")
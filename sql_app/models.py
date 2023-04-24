from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric
from sqlalchemy.orm import relationship

from .database import Base

# Spots model

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

# Zones model

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

# Impark model

class Impark(Base):
    __tablename__="impark"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String)
    postalCode = Column(String)
    latitude = Column(Numeric)
    longitude = Column(Numeric)
    lowestMonthlyRate = Column(Numeric)
    coveredParking = Column(Boolean)
    busNearby = Column(Boolean)
    distanceFromCenter = Column(Numeric)
    usage = Column(Boolean)
    rangePointFive = Column(Numeric)
    rangeOnePointZero = Column(Numeric)
    rangeOnePointFive = Column(Numeric)
    rangeTwoPointZero = Column(Numeric)
    hourlyRate = Column(Numeric)
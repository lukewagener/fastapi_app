from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Decimal
from sqlalchemy.orm import relationship

from .database import Base


class Properties(Base):
    __tablename__ = "properties"

    propertyGuid = Column("PropertyGuid", String)
    # zoneGuid = Column("ZoneGuid", String, ForeignKey("zones.zoneGuid"))
    propertyName = Column("PropertyName", String)
    zoneName = Column("ZoneName", String)
    address = Column("Address", String)
    postalCode = Column("Postal code", String)
    latitude = Column("Latitude", Decimal)
    longitude = Column("Longitude", Decimal)
    coveredParking = Column("Covered Parking", Boolean)
    electricCharger = Column("Electric charger for EV", Boolean) 
    blockHeater = Column("Block Heater", Boolean)
    rating = Column("Rating", Decimal)
    reservationCount = Column("ReservationCount", Integer)
    reservedHours = Column("ReservedHours", Integer)
    spotCount = Column("SpotCount", Integer)

    zoneGuid = relationship(Zones, back_populates="zoneGuid")


class Zones(Base):
    __tablename__ = "zones"

    propertyName = Column("PropertyName", String)
    # zoneGuid = Column("ZoneGuid", String)
    zoneName = Column("ZoneName", String)
    hourly = Column("Hourly", Decimal)
    dailyRate = Column("Daily rate", Decimal)
    eveningRate = Column("Evening rate", Integer)
    fullRate = Column("24/7", Integer)
    commuter = Column("Commuter", Integer)
    eveningsWeekends = Column("Evenings & Weekends", Integer)

    zoneGuid = relationship(Properties, back_populates="zones")
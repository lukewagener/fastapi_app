from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL
URL = "mysql+pymysql://gryd_dev:password@localhost/gryd_db"

# Database engine

engine = create_engine(
    URL
)

# Database session

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
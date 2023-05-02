from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load hidden environment variables

load_dotenv()

# Database URL
URL = os.getenv('SQLALCHEMY_DATABASE_URL')

# Database engine

engine = create_engine(
    URL
)

# Database session

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import read, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/spots/", response_model=list[schemas.Spots])
def read_spots(skip: int = 0, db: Session = Depends(get_db)):
    spots = read.get_spots(db, skip=skip)
    return spots
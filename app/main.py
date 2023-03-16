from fastapi import Depends, FastAPI, HTTPException, Request, Response
from sqlalchemy.orm import Session

from . import models, schemas

from . import crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Middleware
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# All spots endpoint
@app.get("/spots/", response_model=list[schemas.Spot])
def read_spots(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    spots = crud.get_spots(db, skip=skip, limit=limit)
    return spots

# Filter spot by ID endpoint
@app.get("/spots/{id}", response_model=schemas.Spot)
def read_spot(id: int, db: Session = Depends(get_db)):
    spot = crud.get_spot(db, id=id)
    if spot is None:
        raise HTTPException(status_code=404, detail="Spot not found")
    return spot

# All spots with daily rates
@app.get("/spots/pricing/", response_model=schemas.SpotPriced)
def read_spots_pricing(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    spots_priced = crud.get_prices(db, skip=skip, limit=limit)
    print(spots_priced)
    return spots_priced
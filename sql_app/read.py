from sqlalchemy.orm import Session

from . import models, schemas

def get_properties(db: Session, skip: int = 0):
    return db.query(models.Properties).offset(skip).all()
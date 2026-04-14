from fastapi import APIRouter,Depends
from database import SessionLocal
from sqlalchemy.orm import Session
from models.offer import Offer

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/offers")
def get_offers(db: Session = Depends(get_db)):
    return db.query(Offer).all()
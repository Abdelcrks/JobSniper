from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from models.offer import Offer
from database import get_db

router = APIRouter()

@router.get("/offers")
def get_offers(db: Session = Depends(get_db)):
    return db.query(Offer).all()
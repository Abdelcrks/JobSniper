from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from models.offer import Offer
from database import get_db
from services.france_travail import get_offers as fetch_offers

router = APIRouter()

@router.get("/offers")
def get_offers(db: Session = Depends(get_db)):
    return fetch_offers()
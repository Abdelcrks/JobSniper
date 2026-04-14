from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from models.profile import Profile
from database import get_db

router = APIRouter()

@router.get("/profiles")
def get_profiles(db: Session = Depends(get_db)):
    return db.query(Profile).all()
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from models.profile import Profile
from database import get_db
from schemas.profile import ProfileCreate

router = APIRouter()

@router.get("/profiles")
def get_profiles(db: Session = Depends(get_db)):
    return db.query(Profile).all()

@router.post("/profiles")
def create_profile(profile: ProfileCreate, db: Session = Depends(get_db)):
    db_profile = Profile(**profile.model_dump())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile 
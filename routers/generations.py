from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.profile import Profile
from models.generation import Generation
from database import get_db
from services.llm import generate_cover_letter
from services.france_travail import get_offers as fetch_offers

router = APIRouter()

@router.post("/generations")
def create_generation(offer_id: str, profile_id: int, db: Session = Depends(get_db)):
    profil = db.query(Profile).filter(Profile.id == profile_id).first()

    offres = fetch_offers()

    for offre in offres:
        if offre["id"] == offer_id:
            offre_trouvee = offre
            break
    letter= generate_cover_letter(profil, offre_trouvee)

    print(letter)

    db_generation = Generation(offer_id= offer_id, letter_cover = letter)
    db.add(db_generation)
    db.commit()
    db.refresh(db_generation)
    return db_generation

   
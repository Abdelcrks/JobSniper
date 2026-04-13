from sqlalchemy import Column, Integer, String, DateTime, Enum, func
from database import Base
import enum


class ContractType(enum.Enum):
    alternance = "alternance"
    stage = "stage"
    cdi = "cdi"
    cdd = "cdd"
    poeic = "poeic"
    poec = "poec"
    freelance = "freelance"

class Offer(Base):
    __tablename__= "offers"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    url = Column(String)
    description = Column(String)
    date = Column(DateTime)
    location = Column(String)
    type_contract = Column(Enum(ContractType))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime)
    
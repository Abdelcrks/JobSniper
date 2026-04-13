from sqlalchemy import Integer, String,DateTime, func, Column, Enum, Boolean 
from database import Base
from models.enum import ContractType,Sex

class Profile(Base):
    __tablename__="profiles"

    id= Column(Integer,primary_key=True, index=True)
    name = Column(String)
    date_birthday = Column(DateTime)
    sex = Column(Enum(Sex))
    experience = Column(String)
    school = Column(String)
    diploma = Column(String)
    formation = Column(String)
    permis = Column(Boolean)
    contract_type = Column(Enum(ContractType))
    localisation = Column(String)
    disponibility = Column(DateTime)
    description = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


from sqlalchemy import Integer, String, Column,ForeignKey,Enum
from database import Base
from models.enum import Level


class Skill(Base):
    __tablename__="skills"

    id= Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer, ForeignKey("profiles.id"))
    name= Column(String)
    level=Column(Enum(Level))
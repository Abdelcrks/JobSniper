from sqlalchemy import Integer, String, Column, ForeignKey
from database import Base

class Project(Base):
    __tablename__="projects"
    
    id = Column(Integer,primary_key =True, index=True)
    profile_id = Column(Integer, ForeignKey("profiles.id"))
    url = Column(String)
    description = Column(String)
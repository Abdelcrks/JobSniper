from sqlalchemy import Integer, String, Column,ForeignKey,DateTime, func
from database import Base

class Generation(Base):
    __tablename__="generations"

    id= Column(Integer, primary_key=True, index=True)
    offer_id = Column(Integer, ForeignKey("offers.id"))
    letter_cover= Column(String)
    created_at = Column(DateTime, default=func.now())

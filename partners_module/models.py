from sqlalchemy import Column, Integer, String
from db import Base

class Partner(Base):
    __tablename__ = "agents"
    id = Column(Integer, primary_key=True)
    company_name = Column(String)
    type = Column(String)
    inn = Column(String)
    kpp = Column(String)
    director_name = Column(String)
    contact_phone = Column(String)
    contact_email = Column(String)
    priority = Column(Integer)

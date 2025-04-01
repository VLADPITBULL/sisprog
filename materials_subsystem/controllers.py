from db import SessionLocal
from models import Material

def get_all_materials():
    session = SessionLocal()
    materials = session.query(Material).all()
    session.close()
    return materials

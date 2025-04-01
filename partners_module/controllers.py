from db import SessionLocal
from models import Partner
from sqlalchemy.exc import SQLAlchemyError

def get_partners(page=1, per_page=10):
    session = SessionLocal()
    try:
        offset = (page - 1) * per_page
        partners = session.query(Partner).offset(offset).limit(per_page).all()
        total = session.query(Partner).count()
        return partners, total
    finally:
        session.close()

def create_partner(data: dict):
    session = SessionLocal()
    try:
        partner = Partner(**data)
        session.add(partner)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        raise e
    finally:
        session.close()

def update_partner(partner_id: int, data: dict):
    session = SessionLocal()
    try:
        partner = session.query(Partner).get(partner_id)
        if not partner:
            raise ValueError("Партнёр не найден")
        for key, value in data.items():
            setattr(partner, key, value)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def delete_partner(partner_id: int):
    session = SessionLocal()
    try:
        partner = session.query(Partner).get(partner_id)
        if not partner:
            raise ValueError("Партнёр не найден")
        session.delete(partner)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

from sqlalchemy.orm import Session
from src.models.league import League


def get_all_leagues(db: Session):
    return db.query(League).all()

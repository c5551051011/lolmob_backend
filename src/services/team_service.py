from sqlalchemy.orm import Session
from src.models.team import Team


def get_teams_by_league(db: Session, league_id):
    return db.query(Team).filter(Team.league_id == league_id).all()

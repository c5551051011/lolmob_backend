from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.dependencies import get_db
from src.schemas.team import TeamOut
from src.services.team_service import get_teams_by_league

router = APIRouter(prefix="/teams", tags=["Teams"])


@router.get("/league/{league_id}", response_model=List[TeamOut])
def read_teams(league_id: str, db: Session = Depends(get_db)):
    teams = get_teams_by_league(db, league_id)
    if teams is None:
        raise HTTPException(status_code=404, detail="League not found")
    return teams

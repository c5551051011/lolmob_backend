from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from src.dependencies import get_db
from src.schemas.league import LeagueOut
from src.services.league_service import get_all_leagues

router = APIRouter(prefix="/leagues", tags=["Leagues"])


@router.get("/", response_model=List[LeagueOut])
def read_leagues(db: Session = Depends(get_db)):
    return get_all_leagues(db)

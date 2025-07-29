from fastapi import FastAPI

from src.db.database import Base, engine
from src.routers import leagues, teams

Base.metadata.create_all(bind=engine)

app = FastAPI(title="롤몹 API MVP")

app.include_router(leagues.router)
app.include_router(teams.router)

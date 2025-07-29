from pydantic import BaseModel
import uuid

class LeagueOut(BaseModel):
    id: uuid.UUID
    name: str
    region: str | None = None
    image_url: str | None = None

    class Config:
        orm_mode = True

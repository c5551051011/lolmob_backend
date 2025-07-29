from pydantic import BaseModel
import uuid

class TeamOut(BaseModel):
    id: uuid.UUID
    name: str
    code: str
    image_url: str | None = None
    league_id: uuid.UUID

    class Config:
        orm_mode = True

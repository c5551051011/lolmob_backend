from pydantic import BaseModel
import uuid

class PlayerOut(BaseModel):
    id: uuid.UUID
    name: str
    real_name: str | None = None
    role: str | None = None
    image_url: str | None = None
    team_id: uuid.UUID

    class Config:
        orm_mode = True

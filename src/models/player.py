import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from src.db.database import Base

class Player(Base):
    __tablename__ = "players"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    real_name = Column(String, nullable=True)
    role = Column(String, nullable=True)
    image_url = Column(String, nullable=True)

    team_id = Column(UUID(as_uuid=True), ForeignKey("teams.id"), nullable=False)
    team = relationship("Team", back_populates="players")

import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from src.db.database import Base

class Team(Base):
    __tablename__ = "teams"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    code = Column(String, nullable=False)
    image_url = Column(String, nullable=True)

    league_id = Column(UUID(as_uuid=True), ForeignKey("leagues.id"), nullable=False)
    league = relationship("League", back_populates="teams")
    players = relationship("Player", back_populates="team")

import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from src.db.database import Base

class League(Base):
    __tablename__ = "leagues"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, unique=True, nullable=False)
    region = Column(String, nullable=True)
    image_url = Column(String, nullable=True)

    teams = relationship("Team", back_populates="league")

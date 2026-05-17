from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(String(1000), nullable=True)
    owner = Column(String(120), nullable=False, default="Unassigned")
    status = Column(String(50), nullable=False, default="Pending")
    complexity = Column(Integer, nullable=False, default=1)
    business_impact = Column(Integer, nullable=False, default=1)
    ai_priority_score = Column(Integer, nullable=False, default=1)
    recommendation = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

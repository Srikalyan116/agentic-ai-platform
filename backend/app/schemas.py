from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=200)
    description: Optional[str] = None
    owner: str = "Unassigned"
    status: str = "Pending"
    complexity: int = Field(1, ge=1, le=5)
    business_impact: int = Field(1, ge=1, le=5)


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    owner: Optional[str] = None
    status: Optional[str] = None
    complexity: Optional[int] = Field(None, ge=1, le=5)
    business_impact: Optional[int] = Field(None, ge=1, le=5)


class TaskResponse(TaskCreate):
    id: int
    ai_priority_score: int
    recommendation: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True

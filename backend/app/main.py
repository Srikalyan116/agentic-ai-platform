from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from .database import Base, engine, get_db
from .models import Task
from .schemas import TaskCreate, TaskUpdate, TaskResponse
from .services import calculate_priority_score, build_recommendation

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI-First Workflow Platform", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "AI-First Workflow Platform"}


@app.post("/tasks", response_model=TaskResponse)
def create_task(payload: TaskCreate, db: Session = Depends(get_db)):
    score = calculate_priority_score(payload.complexity, payload.business_impact)
    task = Task(
        **payload.model_dump(),
        ai_priority_score=score,
        recommendation=build_recommendation(score),
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


@app.get("/tasks", response_model=List[TaskResponse])
def list_tasks(db: Session = Depends(get_db)):
    return db.query(Task).order_by(Task.ai_priority_score.desc()).all()


@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, payload: TaskUpdate, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    updates = payload.model_dump(exclude_unset=True)
    for key, value in updates.items():
        setattr(task, key, value)

    task.ai_priority_score = calculate_priority_score(task.complexity, task.business_impact)
    task.recommendation = build_recommendation(task.ai_priority_score)
    db.commit()
    db.refresh(task)
    return task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}


@app.get("/dashboard")
def dashboard(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return {
        "total": len(tasks),
        "pending": len([t for t in tasks if t.status.lower() == "pending"]),
        "in_progress": len([t for t in tasks if t.status.lower() == "in progress"]),
        "completed": len([t for t in tasks if t.status.lower() == "completed"]),
    }

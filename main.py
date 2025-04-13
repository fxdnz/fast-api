from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List

from database import SessionLocal, engine
from models import Task, Base

# Create tables in the database (only do this if you want to auto-create them)
# Remove or comment out the line below if you're using an existing Django-created table
# Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic models
class TaskCreate(BaseModel):
    title: str
    is_completed: bool = False

class TaskOut(TaskCreate):
    id: int

    class Config:
        orm_mode = True

# Endpoint to fetch all tasks
@app.get("/tasks", response_model=List[TaskOut])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()

# Endpoint to add a new task
@app.post("/tasks", response_model=TaskOut)
def add_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

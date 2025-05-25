from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional

from database import SessionLocal, engine
from models import Task, Base
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = [
    "http://localhost:5173", 
    "https://fastapi-front.netlify.app", # Allow only your frontend during development
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,             # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],               # Allow all HTTP methods
    allow_headers=["*"],               # Allow all headers
)
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

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    is_completed: Optional[bool] = None

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

# Edit task
@app.put("/tasks/{task_id}", response_model=TaskOut)
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    if task.title is not None:
        db_task.title = task.title
    if task.is_completed is not None:
        db_task.is_completed = task.is_completed

    db.commit()
    db.refresh(db_task)
    return db_task

#  Delete task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(db_task)
    db.commit()
    return {"message": "Task deleted successfully"}

# Endpoint to fetch tasks filtered by completion status
@app.get("/tasks/filter", response_model=List[TaskOut])
def get_tasks_by_completion(is_completed: Optional[bool] = None, db: Session = Depends(get_db)):
    if is_completed is not None:
        # Filter tasks by completion status
        return db.query(Task).filter(Task.is_completed == is_completed).all()
    return db.query(Task).all()

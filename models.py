from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Task(Base):
    __tablename__ = "task_task"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    is_completed = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Task(title='{self.title}', completed={self.is_completed})>"
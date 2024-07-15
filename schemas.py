import enum
from typing import Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime


class StatusEnumPy(str, enum.Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: StatusEnumPy = StatusEnumPy.TODO


class TaskCreate(TaskBase):
    pass


class TaskUpdateStatus(BaseModel):
    status: StatusEnumPy


class Task(TaskBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

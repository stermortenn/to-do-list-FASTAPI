from pydantic import BaseModel
from typing import Optional
from datetime import datetime

from models.tasks_model import ProjectStatus
from schemas.user_schema import BaseResponse

class TaskBase(BaseModel):
    task_name: str
    task_desc: Optional[str] = None
    task_status: ProjectStatus = ProjectStatus.NOT_COMPLETED

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase, BaseResponse):
    task_id: int
    task_date: datetime
    user_id: int
    user_name: str

class TaskUpdate(BaseModel):
    task_name: Optional[str] = None
    task_desc: Optional[str] = None
    task_status: Optional[str] = None
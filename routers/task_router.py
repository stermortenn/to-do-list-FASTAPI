from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.db import get_db
from schemas import task_schema
from models import tasks_model
from core.oauth2 import get_current_user

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/create_task", response_model=task_schema.TaskResponse)
def create_task(task: task_schema.TaskCreate, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):

    new_task = tasks_model.Tasks(
        task_name=task.task_name,
        task_desc=task.task_desc,
        task_status=task.task_status,
        user_id=user_id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

@router.get("/tasks/{task_id}", response_model=task_schema.TaskResponse)
def get_tasks(task_id: int, db: Session = Depends(get_db)):
    task = db.query(tasks_model.Tasks).filter(tasks_model.Tasks.task_id == task_id).first()
    
    if not task:
        raise HTTPException(status_code=404, detail="Task was not found")
    return task
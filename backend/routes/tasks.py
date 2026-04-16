from fastapi import APIRouter
from schemas.task import TaskCreate
from services.task_service import create_task, get_tasks, delete_task

router = APIRouter()

@router.post("/tasks")
def add_task(task: TaskCreate):
    return create_task(task)

@router.get("/tasks/{user_id}")
def read_tasks(user_id: int):
    return get_tasks(user_id)

@router.delete("/tasks/{task_id}")
def remove_task(task_id: str):
    return delete_task(task_id)
from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, func, select

from app.database import get_session
from app.models import Task, TaskCreate, TaskPriority, TaskStatus, TaskUpdate

router = APIRouter(prefix="/api/tasks", tags=["tasks"])


@router.get("/")
def list_tasks(
    status: Optional[TaskStatus] = None,
    priority: Optional[TaskPriority] = None,
    search: Optional[str] = None,
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=10, ge=1, le=100),
    session: Session = Depends(get_session),
):
    """List all tasks with optional filters and pagination."""
    query = select(Task)

    if status:
        query = query.where(Task.status == status)
    if priority:
        query = query.where(Task.priority == priority)
    if search:
        query = query.where(Task.title.contains(search))

    # Count total before pagination
    total = session.exec(select(func.count()).select_from(query.subquery())).one()

    # Apply pagination
    offset = (page - 1) * limit
    tasks = session.exec(query.offset(offset).limit(limit)).all()

    return {
        "success": True,
        "data": tasks,
        "pagination": {
            "page": page,
            "limit": limit,
            "total": total,
            "totalPages": (total + limit - 1) // limit,
        },
    }


@router.get("/{task_id}")
def get_task(task_id: int, session: Session = Depends(get_session)):
    """Get a single task by ID."""
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"success": True, "data": task}


@router.post("/", status_code=201)
def create_task(body: TaskCreate, session: Session = Depends(get_session)):
    """Create a new task."""
    task = Task.model_validate(body)
    session.add(task)
    session.commit()
    session.refresh(task)
    return {"success": True, "data": task}


@router.put("/{task_id}")
def update_task(
    task_id: int, body: TaskUpdate, session: Session = Depends(get_session)
):
    """Update an existing task (partial update)."""
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    update_data = body.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(task, key, value)
    task.updated_at = datetime.utcnow()

    session.add(task)
    session.commit()
    session.refresh(task)
    return {"success": True, "data": task}


@router.delete("/{task_id}")
def delete_task(task_id: int, session: Session = Depends(get_session)):
    """Delete a task."""
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    session.delete(task)
    session.commit()
    return {"success": True, "message": "Task deleted"}

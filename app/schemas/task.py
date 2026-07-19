"""Task Pydantic schemas."""

from datetime import datetime
from uuid import UUID
from typing import Optional

from pydantic import BaseModel

from app.models.task import TaskStatus, TaskPriority


class TaskCreate(BaseModel):
    """Schema for creating a task."""
    title: str
    description: Optional[str] = None
    priority: TaskPriority = TaskPriority.MEDIUM


class TaskUpdate(BaseModel):
    """Schema for updating a task (partial update)."""
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None


class TaskResponse(BaseModel):
    """Schema for task response."""
    id: UUID
    title: str
    description: Optional[str] = None
    status: TaskStatus
    priority: TaskPriority
    user_id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class PaginatedTasks(BaseModel):
    """Schema for paginated task list."""
    items: list[TaskResponse]
    total: int
    page: int
    page_size: int
    total_pages: int

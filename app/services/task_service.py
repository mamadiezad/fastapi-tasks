"""Task service — business logic for task operations."""

from uuid import UUID
from typing import Optional

from sqlalchemy import select, func, or_
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.task import Task, TaskStatus, TaskPriority
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse, PaginatedTasks


class TaskService:
    """Handles task CRUD operations."""

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_task(self, task_data: TaskCreate, user_id: UUID) -> Task:
        """Create a new task for the given user."""
        task = Task(
            title=task_data.title,
            description=task_data.description,
            priority=task_data.priority,
            user_id=user_id,
        )
        self.db.add(task)
        await self.db.flush()
        await self.db.refresh(task)
        return task

    async def get_tasks(
        self,
        user_id: UUID,
        page: int = 1,
        page_size: int = 20,
        status: Optional[TaskStatus] = None,
        priority: Optional[TaskPriority] = None,
        search: Optional[str] = None,
    ) -> PaginatedTasks:
        """Get paginated, filtered list of tasks for a user."""
        query = select(Task).where(Task.user_id == user_id)

        if status:
            query = query.where(Task.status == status)
        if priority:
            query = query.where(Task.priority == priority)
        if search:
            query = query.where(
                or_(
                    Task.title.ilike(f"%{search}%"),
                    Task.description.ilike(f"%{search}%"),
                )
            )

        # Count total
        count_query = select(func.count()).select_from(query.subquery())
        total = (await self.db.execute(count_query)).scalar()

        # Paginate
        query = query.order_by(Task.created_at.desc())
        query = query.offset((page - 1) * page_size).limit(page_size)

        result = await self.db.execute(query)
        tasks = result.scalars().all()

        return PaginatedTasks(
            items=[TaskResponse.model_validate(t) for t in tasks],
            total=total,
            page=page,
            page_size=page_size,
            total_pages=max(1, (total + page_size - 1) // page_size),
        )

    async def get_task(self, task_id: UUID, user_id: UUID) -> Optional[Task]:
        """Get a single task by ID (scoped to user)."""
        result = await self.db.execute(
            select(Task).where(Task.id == task_id, Task.user_id == user_id)
        )
        return result.scalar_one_or_none()

    async def update_task(
        self, task_id: UUID, task_data: TaskUpdate, user_id: UUID
    ) -> Optional[Task]:
        """Update a task (partial update)."""
        task = await self.get_task(task_id, user_id)
        if not task:
            return None

        update_data = task_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(task, field, value)

        await self.db.flush()
        await self.db.refresh(task)
        return task

    async def delete_task(self, task_id: UUID, user_id: UUID) -> bool:
        """Delete a task. Returns True if deleted, False if not found."""
        task = await self.get_task(task_id, user_id)
        if not task:
            return False
        await self.db.delete(task)
        return True

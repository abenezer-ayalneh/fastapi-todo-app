from pydantic import BaseModel
from datetime import datetime


class TodoBase(BaseModel):
    title: str
    description: str | None = None
    created_at: datetime
    due_date: datetime


class TodoCreate(TodoBase):
    pass


class TodoPut(TodoBase):
    title: str
    description: str
    created_at: datetime
    due_date: datetime


class TodoPatch(TodoBase):
    title: str | None = None
    description: str | None = None
    due_date: datetime | None = None


class Todo(TodoBase):
    id: int

    class Config:
        orm_mode = True

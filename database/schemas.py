from typing import Optional, Union
from pydantic import BaseModel
from datetime import datetime


class TodoBase(BaseModel):
    title: Union[str, None]
    description: Union[str, None]
    created_at: Union[datetime, None]
    due_date: Union[datetime, None]


class TodoCreate(TodoBase):
    pass


class TodoPut(TodoBase):
    title: str
    description: str
    created_at: datetime
    due_date: datetime


class TodoPatch(TodoBase):
    title: Union[str, None]
    description: Union[str, None]
    due_date: Union[datetime, None]


class Todo(TodoBase):
    id: int
    title: str
    created_at: str

    class Config:
        orm_mode = True

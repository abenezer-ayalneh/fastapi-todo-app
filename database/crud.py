from sqlalchemy.orm import Session

from . import models, schemas


def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Todo).offset(skip).limit(limit).all()


def create_todo(db: Session, todo: schemas.TodoCreate):
    db_todo = models.Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def update_whole_todo(db: Session, todo_id: int, todo: schemas.TodoPut):
    db_todo = models.Todo
    update_result = db.query(db_todo).\
        filter(db_todo.id == todo_id).update(
        {"title": todo.title, "description": todo.description, 'created_at': todo.created_at, "due_date": todo.due_date})
    db.commit()
    return update_result


def update_todo_partially(db: Session, todo_id: int, todo: schemas.TodoPatch):
    print({**todo.dict()})
    db_todo = models.Todo
    update_result = db.query(db_todo).\
        filter(db_todo.id == todo_id).update({**todo.dict()})
    db.commit()
    return update_result

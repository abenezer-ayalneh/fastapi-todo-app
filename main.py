from pydantic import BaseModel
from typing import Union, List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from database import crud, models, schemas
from database.database import SessionLocal, engine

app = FastAPI()


models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/todos/", response_model=schemas.Todo)
def create_todo(
    todo: schemas.TodoCreate, db: Session = Depends(get_db)
):
    return crud.create_todo(db=db, todo=todo)


@app.get("/todos/", response_model=List[schemas.Todo])
def read_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = crud.get_todos(db, skip=skip, limit=limit)
    return todos


@app.put("/todos/{todo_id}", response_model=int)
def update_todos(todo_id: int, todo: schemas.TodoPut, db: Session = Depends(get_db)):
    return crud.update_whole_todo(db=db, todo_id=todo_id, todo=todo)


@app.patch("/todos/{todo_id}", response_model=int)
def update_todos(todo_id: int, todo: schemas.TodoPatch, db: Session = Depends(get_db)):
    return crud.update_todo_partially(db=db, todo_id=todo_id, todo=todo)

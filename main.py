from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy.orm import Session
from database import sessionlocal, engine
from models import TodoModel

app = FastAPI()

# Create the tables in the database (if not already created)
TodoModel.metadata.create_all(bind=engine)


# like asking for a notebook to write in
def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()


# Pydantic models for request/response

# Base model for Todo (used for creating and displaying todos)
class TodoBase(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

    class Config:
        from_attributes = True  # Enable Pydantic to read SQLAlchemy models


# Get all todos
@app.get("/todos", response_model=List[TodoBase])
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(TodoModel).all()  # Query all todos from the database
    return todos


# Get a specific todo by ID
@app.get("/todos/{todo_id}", response_model=TodoBase)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()  # Query for the todo by ID

    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    return todo


# Create a new todo
@app.post("/todos", response_model=TodoBase)
def create_todo(todo: TodoBase, db: Session = Depends(get_db)):
    db_todo = TodoModel(id = todo.id, title=todo.title, description=todo.description, completed=todo.completed)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)  # Ensure the newly created record is updated with the ID
    return db_todo


# Delete a todo by ID
@app.delete("/todos/{todo_id}", response_model=TodoBase)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return todo


# Update an existing todo by ID
@app.put("/todos/{todo_id}", response_model=TodoBase)
def update_todo(todo_id: int, todo: TodoBase, db: Session = Depends(get_db)):
    db_todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    # Update the todo with the new values
    db_todo.id = todo.id
    db_todo.title = todo.title
    db_todo.description = todo.description
    db_todo.completed = todo.completed
    db.commit()
    db.refresh(db_todo)  # Refresh the instance with updated values
    return db_todo















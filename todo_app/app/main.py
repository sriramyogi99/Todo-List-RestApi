from fastapi import FastAPI, HTTPException, Query, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from typing import List
from .schemas import TodoCreate, TodoUpdate
from .models import Todo
from . import crud

app = FastAPI()

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")


# Basic Authentication
security = HTTPBasic()

# Mock user database (replace with actual user validation logic)
users_db = {
    "user1": {
        "username": "user1",
        "password": "password1",
    }
}


# Authentication function
def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    """
    Authenticate user using basic authentication.
    :param credentials: HTTPBasicCredentials containing the username and password.
    :return: Username if authentication is successful.
    :raises HTTPException: If authentication fails.
    """
    user = users_db.get(credentials.username)
    if not user or user["password"] != credentials.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
            headers={"WWW-Authenticate": "Basic"},
        )
    return user["username"]


# Home page endpoint
@app.get("/")
def read_root():
    """
    Serve the home page.
    :return: HTML file of the home page.
    """
    return FileResponse("static/index.html")


# Endpoint to create a new todo item
@app.post("/todos/", response_model=Todo)
def create_todo_item(todo_create: TodoCreate):
    """
    Create a new todo item.
    :param todo_create: TodoCreate schema with the data to create a new todo.
    :return: The created todo item.
    """
    todo = crud.create_todo(todo_create)
    return todo


# Endpoint to read all todo items with pagination
@app.get("/todos/", response_model=List[Todo])
def read_all_todo_items(skip: int = Query(0, ge=0), limit: int = Query(15, le=50), username: str = Depends(authenticate)):
    """
    Retrieve all todo items with pagination.
    :param skip: Number of items to skip (default: 0).
    :param limit: Maximum number of items to return (default: 15).
    :param username: Authenticated username.
    :return: List of todo items.
    """
    return crud.get_all_todos(skip=skip, limit=limit)


# Endpoint to read a specific todo item by ID
@app.get("/todos/{todo_id}", response_model=Todo)
def read_todo_item(todo_id: int):
    """
    Retrieve a specific todo item by its ID.
    :param todo_id: ID of the todo item to retrieve.
    :return: The todo item if found.
    :raises HTTPException: If the todo item is not found.
    """
    todo = crud.get_todo_by_id(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail=f"Item with ID {todo_id} not found.")
    return todo


# Endpoint to update a specific todo item by ID
@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo_item(todo_id: int, todo_update: TodoUpdate):
    """
    Update a specific todo item by its ID.
    :param todo_id: ID of the todo item to update.
    :param todo_update: TodoUpdate schema with the updated data.
    :return: The updated todo item if found.
    :raises HTTPException: If the todo item is not found.
    """
    todo = crud.update_todo(todo_id, todo_update)
    if todo is None:
        raise HTTPException(status_code=404, detail=f"Item with ID {todo_id} not found.")
    return todo


# Endpoint to delete a specific todo item by ID
@app.delete("/todos/{todo_id}", response_model=Todo)
def delete_todo_item(todo_id: int):
    """
    Delete a specific todo item by its ID.
    :param todo_id: ID of the todo item to delete.
    :return: Confirmation message if the deletion is successful.
    :raises HTTPException: If the todo item is not found.
    """
    todo = crud.delete_todo(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail=f"Item with ID {todo_id} not found.")
    return {"message": f"Todo item with ID {todo_id} deleted successfully."}

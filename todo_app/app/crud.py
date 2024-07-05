from typing import List, Optional
from .models import Todo
from .schemas import TodoCreate, TodoUpdate
import random
from fastapi import HTTPException

# In-memory storage for todo items
todos: List[Todo] = []
next_id: int = 1

# Create 20 random todos
# This loop creates 20 sample todo items and inserts them at the beginning of the todos list.
for i in range(20):
    todo = Todo(
        id=next_id,
        title=f"Sample Todo {i + 1}",
        description=f"This is a description for sample todo {i + 1}",
        completed=False
    )
    todos.insert(0, todo) # Insert each new todo at the beginning
    next_id += 1 # Increment the ID for the next todo


# Function to get all todos with pagination
def get_all_todos(skip: int = 0, limit: int = 15):
    """
    Retrieve a paginated list of todo items.
    :param skip: Number of items to skip (default: 0).
    :param limit: Maximum number of items to return (default: 15).
    :return: List of todo items.
    """
    return todos[skip: skip + limit]


# Function to get a single todo by ID
def get_todo_by_id(todo_id: int) -> Optional[Todo]:
    """
    Retrieve a todo item by its ID.
    :param todo_id: ID of the todo item to retrieve.
    :return: The todo item if found, otherwise None.
    """
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return None


# Function to create a new todo
def create_todo(todo_create: TodoCreate) -> Todo:
    """
    Create a new todo item.
    :param todo_create: The data required to create a new todo.
    :return: The created todo item.
    """
    global next_id
    todo = Todo(
        id=next_id,
        title=todo_create.title,
        description=todo_create.description
    )
    todos.insert(0, todo)  # Insert new todo at the beginning
    next_id += 1 # Increment the ID for the next todo
    return todo


# Function to update an existing todo
def update_todo(todo_id: int, todo_update: TodoUpdate) -> Optional[Todo]:
    """
    Update an existing todo item.
    :param todo_id: ID of the todo item to update.
    :param todo_update: The updated data for the todo.
    :return: The updated todo item if found, otherwise None.
    """
    for todo in todos:
        if todo.id == todo_id:
            todo.title = todo_update.title
            todo.description = todo_update.description
            todo.completed = todo_update.completed
            return todo
    return None


# Function to delete a todo
def delete_todo(todo_id: int) -> Optional[Todo]:
    """
    Delete a todo item by its ID.
    :param todo_id: ID of the todo item to delete.
    :return: The deleted todo item if found, otherwise None.
    """
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return todo
    return None



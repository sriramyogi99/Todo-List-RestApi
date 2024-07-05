# FastAPI Todo App

This is a simple Todo application built with FastAPI that allows users to manage todo items through a RESTful API.

## Prerequisites

Before running this application, ensure you have the following installed:

- Python (version 3.7 or higher)
- pip (Python package installer)

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone <repository_url>
   cd fastapi-todo-app
    ```
2. Create a virtual environment (optional but recommended):

    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate


3. Install the required Python packages:
    
    pip install -r requirements.txt

4. Running the Application

    (i) Start the FastAPI application:

        uvicorn main:app --reload

    This command runs the FastAPI application (main refers to your main Python file, and app is the instance of FastAPI created).

    (ii) Open your web browser and go to http://localhost:8000 to access the application.

        API Endpoints:

            GET /todos/: Retrieve all todo items.
            POST /todos/: Create a new todo item.
            GET /todos/{todo_id}: Retrieve a specific todo item by ID.
            PUT /todos/{todo_id}: Update a specific todo item by ID.
            DELETE /todos/{todo_id}: Delete a specific todo item by ID.

        Authentication:

            Basic Authentication is implemented to secure the API endpoints.
            Use the following credentials to authenticate:
                Username: user1
                Password: password1



FastAPI Todo App
A simple Todo application built using FastAPI, SQLAlchemy, and a MySQL database. This app allows you to manage your todo items with CRUD operations.

Features:
Create, Read, Update, Delete (CRUD) operations for todos.
FastAPI for building the API.
SQLAlchemy for database interaction.
PM2 for process management.
Tested with Postman.
Prerequisites
Python 3.8+
MySQL Database
PM2 (optional, for production deployment)
Postman (for testing APIs)
Setup Instructions
Clone the Repository:

bash
Copy code
git clone https://github.com/ruquiyaanjum/FAST_API_TODOS.git
cd FAST_API_TODOS
Set up the Database:

Create a .env file in the root of the project with your MySQL connection details:

bash
Copy code
DATABASE_URL=mysql+pymysql://username:password@localhost/db_name
Install Dependencies:

Install the required Python libraries:

bash
Copy code
pip install -r requirements.txt
Run the App with Uvicorn:

Start the FastAPI app locally:

bash
Copy code
uvicorn main:app --host 0.0.0.0 --port 8000
The app will be available at http://localhost:8000.

Using PM2 (For Production)
To keep your FastAPI app running in the background with PM2, follow these steps:

Install PM2 globally:

bash
Copy code
npm install pm2 -g
Start your FastAPI app with PM2:

bash
Copy code
pm2 start "uvicorn main:app --host 0.0.0.0 --port 8000" --name fastapi-todo
This will run the app in the background and restart it automatically if it crashes.

To view logs:

bash
Copy code
pm2 logs fastapi-todo
To stop the app:

bash
Copy code
pm2 stop fastapi-todo
API Endpoints
GET /todos: Get all todos.
GET /todos/{todo_id}: Get a specific todo by ID.
POST /todos: Create a new todo.
PUT /todos/{todo_id}: Update an existing todo by ID.
DELETE /todos/{todo_id}: Delete a todo by ID.
Testing with Postman
Use Postman to test the following API endpoints:

GET /todos: Fetch all todos.

GET /todos/{todo_id}: Fetch a specific todo by ID.

POST /todos: Create a new todo with a JSON body:

json
Copy code
{
    "id": 1,
    "title": "Sample Todo",
    "description": "This is a sample description.",
    "completed": false
}
PUT /todos/{todo_id}: Update an existing todo.

DELETE /todos/{todo_id}: Delete a todo.

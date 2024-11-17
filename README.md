# FastAPI Todo App

A simple Todo application built using **FastAPI**, **SQLAlchemy**, and a **MySQL** database. This app allows you to manage your todo items with CRUD operations.

### Features:
- Create, Read, Update, Delete (CRUD) operations for todos.
- **FastAPI** for building the API.
- **SQLAlchemy** for database interaction.
- **PM2** for process management.
- Tested with **Postman**.

---

### Prerequisites

- Python 3.8+
- MySQL Database
- PM2 (optional, for production deployment)
- [Postman](https://www.postman.com/) (for testing APIs)

---

### Setup Instructions

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/ruquiyaanjum/FAST_API_TODOS.git
    cd FAST_API_TODOS
    ```

2. **Set up the Database:**

    Create a `.env` file in the root of the project with your MySQL connection details:

    ```
    DATABASE_URL=mysql+pymysql://username:password@localhost/db_name
    ```

3. **Install Dependencies:**

    Install the required Python libraries:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the App with Uvicorn:**

    Start the FastAPI app locally:

    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```

    The app will be available at `http://localhost:8000`.

---

### Using PM2 (For Production)

To keep your FastAPI app running in the background with **PM2**, follow these steps:

1. Install **PM2** globally:

    ```bash
    npm install pm2 -g
    ```

2. Start your FastAPI app with **PM2**:

    ```bash
    pm2 start "uvicorn main:app --host 0.0.0.0 --port 8000" --name fastapi-todo
    ```

    This will run the app in the background and restart it automatically if it crashes.

3. To view logs:

    ```bash
    pm2 logs fastapi-todo
    ```

4. To stop the app:

    ```bash
    pm2 stop fastapi-todo
    ```

---

### API Endpoints

- **GET `/todos`**: Get all todos.
- **GET `/todos/{todo_id}`**: Get a specific todo by ID.
- **POST `/todos`**: Create a new todo.
- **PUT `/todos/{todo_id}`**: Update an existing todo by ID.
- **DELETE `/todos/{todo_id}`**: Delete a todo by ID.

---

### Testing with Postman

Use **Postman** to test the following API endpoints:

- **GET /todos**: Fetch all todos.
- **GET /todos/{todo_id}**: Fetch a specific todo by ID.
- **POST /todos**: Create a new todo with a JSON body:

    ```json
    {
        "id": 1,
        "title": "Sample Todo",
        "description": "This is a sample description.",
        "completed": false
    }
    ```

- **PUT /todos/{todo_id}**: Update an existing todo.
- **DELETE /todos/{todo_id}**: Delete a todo.

---

### License

This project is licensed under the MIT License.


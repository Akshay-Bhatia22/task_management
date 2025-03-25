# Task Management Service

## Overview
This API service allows users to manage tasks by creating, updating, deleting, and assigning them to users.

## Setting Up

### Step 1: Create and Activate Virtual Environment
```sh
python -m venv venv
```
Activate the virtual environment:
- **Windows:**
  ```sh
  venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```sh
  source venv/bin/activate
  ```
Once activated, your terminal prompt should show `(venv)` indicating the virtual environment is active.

### Step 2: Install Dependencies
```sh
pip install -r requirements.txt
```

### Step 3: Apply Database Migrations
```sh
python manage.py migrate
```

### Step 4: Run the Development Server
```sh
python manage.py runserver 8080
```
This will start the server on `http://127.0.0.1:8080/`.


## API Documentation
## **1. Create a Task**
### **Endpoint:** `POST /api/task/tasks/`
**Description:** Allows the creation of new tasks with a name, description, and status.

**Authorization:**
```
Authorization: Bearer <access_token>
```

**Request Body:**
```json
{
    "name": "Develop API",
    "description": "Create API endpoints",
    "task_type": "backend",
    "completed_at": "2025-04-01T12:00:00Z",
    "status": "TO DO"
}
```

**Response:**
```json
{
    "id": 1,
    "name": "Develop API",
    "description": "Create API endpoints",
    "task_type": "backend",
    "created_at": "2025-03-24T19:08:55.783965Z",
    "created_by": 2,
    "completed_at": "2025-04-01T12:00:00Z",
    "status": "TO DO",
    "assignee": [3, 4]
}
```

---

## **2. Assign a Task to a User**
### **Endpoint:** `PATCH /api/task/assign/<int:task_id>`
**Description:** Assigns a task to one or multiple users.

**Authorization:**
```
Authorization: Bearer <access_token>
```

**Request Body:**
```json
{
    "user": [3, 4],
    "operation": "add"
}
```

**Response (Adding users):**
```json
{
    "message": "Assigned user ids [3, 4] successfully."
}
```

**Response (Removing users):**
```json
{
    "message": "Assigned user ids [3] deleted successfully."
}
```

---

## **3. Get Tasks for a Specific User**
### **Endpoint:** `GET /api/task/by_assignee/<int:user_id>`
**Description:** Fetch all tasks assigned to a particular user.

**Authorization:**
```
Authorization: Bearer <access_token>
```

**Response:**
```json
[
    {
        "id": 1,
        "name": "Develop API",
        "description": "Create API endpoints",
        "task_type": "backend",
        "created_at": "2025-03-24T19:08:55.783965Z",
        "created_by": 2,
        "completed_at": "2025-04-01T12:00:00Z",
        "status": "TO DO",
        "assignee": [3, 4]
    }
]
```

---

## **4. Get All Tasks of Logged-in User**
### **Endpoint:** `GET /api/task/tasks`
**Description:** Fetch all tasks created by the logged-in user.

**Authorization:**
```
Authorization: Bearer <access_token>
```

**Response:**
```json
[
    {
        "id": 2,
        "name": "Fix Bug",
        "description": "Resolve login issue",
        "task_type": "frontend",
        "created_at": "2025-03-25T10:30:00.000Z",
        "created_by": 1,
        "completed_at": null,
        "status": "IN PROGRESS",
        "assignee": [5]
    }
]
```

---

## **5. Delete a Task**
### **Endpoint:** `DELETE /api/task/tasks/<int:task_id>`
**Description:** Deletes a specific task by its ID.

**Authorization:**
```
Authorization: Bearer <access_token>
```

**Response:**
```json
{
    "message": "Task deleted successfully."
}
```

---

## **6. Update a Task**
### **Endpoint:** `PUT /api/task/tasks/<int:task_id>`
**Description:** Updates an existing task.

**Authorization:**
```
Authorization: Bearer <access_token>
```

**Request Body:**
```json
{
    "name": "Refactor Code",
    "description": "Improve code quality",
    "status": "IN PROGRESS"
}
```

**Response:**
```json
{
    "id": 3,
    "name": "Refactor Code",
    "description": "Improve code quality",
    "task_type": "backend",
    "created_at": "2025-03-26T09:15:00.000Z",
    "created_by": 2,
    "completed_at": null,
    "status": "IN PROGRESS",
    "assignee": [6]
}
```

---

## **7. User Signup**
### **Endpoint:** `POST /api/signup`
**Description:** Creates a new user account.

**Request Body:**
```json
{
    "email":"john@example.com",
    "name":"John Doe",
    "mobile":"9876543210",
    "password":"securepassword",
    "gender":"male",
    "position":"developer"
}
```

---

## **8. User Login**
### **Endpoint:** `POST /api/login`
**Description:** Authenticates a user and returns access tokens.

**Request Body:**
```json
{
    "email":"john@example.com",
    "password":"securepassword"
}
```

**Response:**
```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```
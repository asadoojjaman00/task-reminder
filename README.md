# 📝 Task Reminder API

A **Task Reminder** backend application built with **Django & Django REST Framework** that allows users to manage their personal tasks and receive **email notifications at scheduled reminder times**. The project focuses on **clean architecture, secure authentication, and asynchronous task processing**, making it recruiter‑friendly and production‑oriented.

---

## 🚀 Features

* 🔐 **User Authentication** using JWT (Access & Refresh Tokens)
* 👤 **User Registration, Login, Logout**
* 🗂️ **CRUD operations on Tasks** (Create, Read, Update, Delete)
* 🔒 Users can manage **only their own tasks**
* ⏰ **Task Reminder System** with scheduled email notifications
* ⚙️ **Asynchronous background jobs** using Celery
* 🚀 **Redis** as message broker for task scheduling
* 🧼 Clean, RESTful API design

---

## 🛠️ Tech Stack

| Category          | Technology                    |
| ----------------- | ----------------------------- |
| Language          | Python                        |
| Backend Framework | Django                        |
| API Framework     | Django REST Framework (DRF)   |
| Authentication    | JWT (Access & Refresh Tokens) |
| Background Tasks  | Celery                        |
| Message Broker    | Redis                         |
| Database          | SQLite (development)          |

---

## 📦 Project Use Case

This project is designed for users who want to:

* Create personal tasks
* Set a **specific reminder time** for each task
* Receive an **email notification automatically** when the reminder time is reached

The reminder system runs asynchronously using **Celery**, ensuring that scheduled emails are sent **without blocking the main application**.

---

## 🔐 Authentication Flow

* User registers with email & password
* User logs in and receives **Access Token & Refresh Token**
* Access token is used to access protected APIs
* Refresh token is used to generate a new access token
* Logout invalidates the active token

---

## 📡 API Endpoints

### 🔑 Authentication APIs

```http
POST /api/register/
POST /api/login/
POST /api/login/refresh/
POST /api/logout/
```

**Responsibilities:**

* User registration
* JWT token generation
* Token refresh
* Secure logout

---

### 🗂️ Task APIs

```http
GET    /api/tasks/
POST   /api/tasks/
GET    /api/tasks/<id>/
PUT    /api/tasks/<id>/
DELETE /api/tasks/<id>/
```

**Responsibilities:**

* Create a task with reminder time
* View all tasks of the authenticated user
* Update existing tasks
* Delete tasks

🔒 **Access Control:** Users can only access and modify their own tasks.

---

## 🧠 Background Task Processing

* When a task is created or updated with a reminder time:

  * A Celery task is scheduled
  * Celery waits until the reminder time
  * An **email notification** is sent automatically

This ensures:

* Non‑blocking request handling
* Scalable reminder scheduling

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone <repository-url>
cd task-reminder
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Migrations

```bash
python manage.py migrate
```

### 5️⃣ Start Redis Server

```bash
redis-server
```

### 6️⃣ Run Celery Worker

```bash
celery -A config worker -l info
```

### 7️⃣ Start Django Server

```bash
python manage.py runserver
```

---

## 🧪 API Testing

* Postman
* JWT authentication supported
* Token-based secured endpoints

---

## 📌 Future Improvements

* ⏱️ Celery Beat for recurring reminders
* 📧 Email template customization
* 🗄️ PostgreSQL support
* 🐳 Docker setup
* 📊 Task analytics & filtering

---

## 👨‍💻 Author

**Asif (Asadoojjaman)**
Backend Developer | Python | Django | DRF

---

## ⭐ Recruiter Note

This project demonstrates:

* Real‑world backend architecture
* Secure authentication with JWT
* Asynchronous task handling with Celery
* Clean REST API design
* Ownership‑based data access control

Ideal for showcasing **backend engineering skills** in interviews and production‑level projects.

---

📩 *Feel free to fork, explore, and contribute!*

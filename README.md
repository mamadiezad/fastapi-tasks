# FastAPI Tasks 📋

A production-ready RESTful Task Management API built with **FastAPI**, **SQLAlchemy**, **PostgreSQL**, and **JWT Authentication**.

## ✨ Features

- ✅ **JWT Authentication** — Secure login & registration
- ✅ **CRUD Operations** — Create, read, update, delete tasks
- ✅ **Filtering & Pagination** — Search by status, priority, date
- ✅ **Async Database** — SQLAlchemy async with PostgreSQL
- ✅ **Docker Support** — Fully containerized
- ✅ **Comprehensive Tests** — Pytest with coverage
- ✅ **OpenAPI Docs** — Auto-generated Swagger & ReDoc
- ✅ **Rate Limiting** — Protect API from abuse

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| **FastAPI** | Web framework |
| **SQLAlchemy** | ORM (async) |
| **PostgreSQL** | Database |
| **Redis** | Caching & rate limiting |
| **Docker** | Containerization |
| **Pytest** | Testing |
| **Alembic** | Migrations |

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/mamadiezad/fastapi-tasks.git
cd fastapi-tasks

# Install dependencies
pip install -r requirements.txt

# Run with Docker
docker-compose up --build

# Or run locally
uvicorn app.main:app --reload
```

## 📖 API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/auth/register` | Register new user |
| POST | `/api/v1/auth/login` | Login & get JWT token |
| POST | `/api/v1/auth/refresh` | Refresh access token |

### Tasks
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/tasks` | List tasks (paginated) |
| POST | `/api/v1/tasks` | Create a task |
| GET | `/api/v1/tasks/{id}` | Get task details |
| PUT | `/api/v1/tasks/{id}` | Update a task |
| DELETE | `/api/v1/tasks/{id}` | Delete a task |

## 📊 Database Schema

```sql
users (
    id UUID PRIMARY KEY,
    email VARCHAR UNIQUE NOT NULL,
    username VARCHAR UNIQUE NOT NULL,
    hashed_password VARCHAR NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
)

tasks (
    id UUID PRIMARY KEY,
    title VARCHAR NOT NULL,
    description TEXT,
    status ENUM(todo, in_progress, done),
    priority ENUM(low, medium, high),
    user_id UUID REFERENCES users(id),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
)
```

## 🧪 Testing

```bash
# Run tests
pytest

# With coverage
pytest --cov=app --cov-report=html

# Run specific test
pytest tests/test_tasks.py -v
```

## 📄 License

MIT License — feel free to use this project for learning or as a starter template.

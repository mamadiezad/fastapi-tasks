# FastAPI Tasks — Production-Ready Task Management API 🚀

> **FastAPI** + **PostgreSQL** + **JWT Authentication** + **Docker** — The complete task management REST API for your next project.

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111-009688?logo=fastapi)](https://fastapi.tiangolo.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?logo=postgresql)](https://postgresql.org)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker)](https://docker.com)
[![Tests](https://img.shields.io/badge/Tests-Passing-success?logo=pytest)](https://docs.pytest.org)

---

## 📋 Overview

**FastAPI Tasks** is a production-ready **task management REST API** built with modern Python technologies. It provides secure user authentication, complete CRUD operations for tasks, advanced filtering with pagination, and is fully containerized with Docker.

Whether you're building a **SaaS product**, learning **FastAPI**, or need a **backend for your task management app** — this is the perfect starting point.

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🔐 **JWT Authentication** | Secure registration, login, and token-based auth |
| 📝 **Task CRUD** | Create, read, update, and delete tasks |
| 🔍 **Advanced Filtering** | Filter by status, priority, and search keywords |
| 📄 **Pagination** | Page-based pagination for large datasets |
| 🐘 **Async PostgreSQL** | High-performance async SQLAlchemy ORM |
| 🐳 **Docker Ready** | Full Docker Compose setup with DB & Redis |
| 🧪 **Test Coverage** | Comprehensive pytest suite with async support |
| 📚 **Auto Docs** | Swagger UI & ReDoc generated automatically |
| ⚡ **Rate Limiting** | Redis-based rate limiting for API protection |

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| **FastAPI** | High-performance Python web framework |
| **SQLAlchemy** | Async ORM for database operations |
| **PostgreSQL** | Primary database |
| **Redis** | Caching & rate limiting |
| **Docker** | Containerization & deployment |
| **Pytest** | Testing framework |
| **JWT** | Authentication & authorization |

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/mamadiezad/fastapi-tasks.git
cd fastapi-tasks

# Run with Docker (recommended)
docker-compose up --build

# Or run locally
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API will be available at `http://localhost:8000`  
Interactive docs at `http://localhost:8000/docs`

---

## 📖 API Endpoints

### 🔑 Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/v1/auth/register` | Register a new user |
| `POST` | `/api/v1/auth/login` | Login and get JWT token |

### 📋 Tasks
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/v1/tasks` | List tasks (paginated, filterable) |
| `POST` | `/api/v1/tasks` | Create a new task |
| `GET` | `/api/v1/tasks/{id}` | Get task details |
| `PUT` | `/api/v1/tasks/{id}` | Update a task (partial) |
| `DELETE` | `/api/v1/tasks/{id}` | Delete a task |

---

## 🐳 Docker Deployment

```bash
# Build and start all services
docker-compose up --build

# Or run detached
docker-compose up -d

# View logs
docker-compose logs -f api
```

---

## 🧪 Testing

```bash
# Run all tests
pytest

# With coverage report
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/test_auth.py -v
```

---

## 📁 Project Structure

```
fastapi-tasks/
├── app/
│   ├── api/           # API routes (auth, tasks)
│   ├── core/          # Config, security, database
│   ├── models/        # SQLAlchemy models (User, Task)
│   ├── schemas/       # Pydantic schemas
│   └── services/      # Business logic layer
├── tests/             # Pytest test suite
├── Dockerfile         # Docker image
├── docker-compose.yml # Multi-service setup
└── requirements.txt   # Python dependencies
```

---

## 🔗 Related Projects

- [Node GraphQL API](https://github.com/mamadiezad/node-graphql-api) — GraphQL API with Apollo & Prisma
- [React Kanban](https://github.com/mamadiezad/react-kanban) — Drag & drop Kanban board frontend
- [TS Design Patterns](https://github.com/mamadiezad/ts-design-patterns) — Design patterns in TypeScript

---

## 📄 License

**MIT** — Free to use, modify, and distribute.

---

<p align="center">
  <sub>Built with ❤️ by <a href="https://github.com/mamadiezad">Mohammad</a></sub>
</p>
<p align="center">ساخته شده با ❤️ توسط <a href="https://github.com/mamadiezad">Mohammad</a> | <a href="https://t.me/llllxyz">📱 تلگرام</a></p>
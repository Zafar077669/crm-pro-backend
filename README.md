# Apex Marketplace Backend

AI-powered Marketplace Platform backend built with Django and PostgreSQL.

Apex Marketplace is a scalable backend system designed for local commerce platforms, providing product discovery, store management, recommendation services, authentication, and marketplace operations through a RESTful API architecture.

---

## Overview

The project is designed as a modular marketplace backend that can serve web applications, mobile applications, and third-party integrations.

Core objectives:

- Marketplace infrastructure
- Product catalog management
- Shop management
- Regional product discovery
- Favorites and reviews
- JWT authentication
- AI-powered search and recommendations
- Scalable API architecture
- Background task processing

---

## Technology Stack

| Layer | Technology |
|---------|------------|
| Backend | Django 5 |
| API | Django REST Framework |
| Database | PostgreSQL |
| Authentication | JWT (SimpleJWT) |
| Cache | Redis |
| Background Jobs | Celery |
| Scheduler | Celery Beat |
| Documentation | DRF Spectacular (OpenAPI) |
| Reverse Proxy | Nginx |
| Application Server | Gunicorn |
| Containerization | Docker & Docker Compose |

---

## Architecture

The backend follows a modular application structure:

```text
apps/

├── users/
├── regions/
├── shops/
├── categories/
├── products/
├── favorites/
├── reviews/
├── ai/
└── recommendations/
```

Each module is isolated and responsible for a specific business domain.

---

## Main Features

### Authentication

- JWT Access Token
- JWT Refresh Token
- Custom User Model
- Protected Endpoints

### Marketplace

- Product Management
- Category Management
- Shop Management
- Regional Filtering
- Product Search
- Product Reviews
- Favorites System

### AI Services

- AI Search Endpoint
- Recommendation Engine Foundation
- Background Processing with Celery

### Infrastructure

- Redis Caching
- Celery Workers
- Celery Beat Scheduler
- Dockerized Environment
- Nginx Reverse Proxy
- Gunicorn Application Server

---

## API Documentation

OpenAPI schema and Swagger documentation are available through DRF Spectacular.

Example endpoints:

```text
/api/v1/auth/login/
/api/v1/auth/me/
/api/v1/ai/search/
```

---

## Background Services

### Celery Worker

Used for:

- Recommendation generation
- AI processing
- Asynchronous tasks
- Heavy computations

### Celery Beat

Used for:

- Scheduled jobs
- Recommendation updates
- Cache maintenance
- Statistics collection

---

## Development Setup

Clone repository:

```bash
git clone https://github.com/Zafar077669/apex-marketplace-backend.git

cd apex-marketplace-backend
```

Create environment:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Create admin user:

```bash
python manage.py createsuperuser
```

Run development server:

```bash
python manage.py runserver
```

---

## Docker Environment

Start all services:

```bash
docker compose up -d --build
```

Services:

- PostgreSQL
- Redis
- Django Backend
- Celery Worker
- Celery Beat
- Nginx

---

## Current Status

Current implementation includes:

- Django REST API
- PostgreSQL Integration
- Redis Cache Layer
- JWT Authentication
- Celery Integration
- Celery Beat Scheduling
- Docker Infrastructure
- Nginx Reverse Proxy
- Swagger Documentation

The project is actively evolving with additional AI and marketplace features planned.

---

## Author

**Zafar Sharipov**

Python Backend Developer

GitHub:
https://github.com/Zafar077669

# Enterprise AI-Powered Multi-Tenant School Management System

This is a production-ready Django backend for a scalable School Management System.

## Architecture
- **Multi-Tenancy**: Uses `django-tenants` with a shared schema for platform management and individual schemas for each school.
- **Clean Architecture**: Decoupled modules in `apps/` and central configuration in `core/`.
- **Service Layer**: Business logic (GPA calculation, invoicing, AI calls) is extracted into service classes.
- **AI Engine**: Integrated OpenAI API for automated report comments, fee reminders, and risk detection.
- **Real-time**: Django Channels (WebSockets) for instant notifications.
- **Task Queue**: Celery + Redis for background processing.

## Tech Stack
- Django 5.2
- Django Rest Framework (DRF)
- PostgreSQL (Multi-schema)
- Redis (Caching + Celery + Channels)
- Celery (Background tasks)
- OpenAI API
- Docker & Docker Compose

## Setup
1. Clone the repository.
2. Copy `.env.example` to `.env` and fill in the values.
3. Build and run with Docker:
   ```bash
   docker-compose up --build
   ```
4. Create a public tenant (The platform):
   ```bash
   docker-compose exec web python manage.py create_tenant
   ```
5. Run tests:
   ```bash
   pytest
   ```

## Security
- **JWT Auth**: Stateless authentication with SimpleJWT.
- **RBAC**: Role-Based Access Control enforced at the model and view levels.
- **Object-level Permissions**: `django-guardian` for fine-grained access.
- **Audit Logs**: Automatic tracking of user activities.

## API Documentation
Once running, visit:
- Swagger: `http://localhost:8000/api/docs/swagger/`
- Redoc: `http://localhost:8000/api/docs/redoc/`

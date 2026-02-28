# Base Image
FROM python:3.12-slim

# Environments
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Dependencies
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Application code
COPY . /app/

# Port exposure
EXPOSE 8000

# Entry point (to be overridden by docker-compose)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "school_management.wsgi:application"]

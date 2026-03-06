# 1. Base image
FROM python:3.12-slim

# 2. Python environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# 3. System dependencies for PostgreSQL
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# 4. Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy all the content of briefcase-python-api to the WORKDIR
COPY . .

# 6. Execution command
CMD ["gunicorn", "--bind", ":8080", "--workers", "2", "core.wsgi:application"]
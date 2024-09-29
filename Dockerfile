
# pull official base image
FROM python:3.11.1-alpine

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN echo "Installing dependencies"
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Copy the .env file into the container
COPY .env /app/.env

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Expose the port on which the WSGI server will run
EXPOSE 8000

# Run migrations
RUN python manage.py makemigrations
RUN python manage.py migrate

# Run the WSGI server command when the container starts
CMD gunicorn cache_service.wsgi:application --bind 0.0.0.0:8003

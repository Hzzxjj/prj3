# Use Python 3.10 as the base image
FROM public.ecr.aws/docker/library/python:3.10-alpine

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apk add --no-cache gcc musl-dev postgresql-dev

# Copy requirements and install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY analytics/ /app/

# Create a non-root user for security
RUN adduser -D -s /bin/sh appuser && chown -R appuser:appuser /app
USER appuser

# Expose port 5153
EXPOSE 5153

# Set environment variables
ENV APP_PORT=5153
ENV PYTHONUNBUFFERED=1

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:5153/health_check')" || exit 1

# Run the application
CMD ["python", "app.py"]
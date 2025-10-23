#!/bin/bash

# Deployment script for Render
echo "Starting deployment..."

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run database migrations
echo "Running database migrations..."
alembic upgrade head

# Start the application
echo "Starting application..."
uvicorn app.main:app --host 0.0.0.0 --port $PORT

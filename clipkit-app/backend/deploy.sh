#!/bin/bash

# Deployment script for Render
echo "Starting deployment..."

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run database migrations
echo "Running database migrations..."
alembic upgrade head

echo "Deployment script completed successfully!"

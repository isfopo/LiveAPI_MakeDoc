#!/bin/bash

# Script to run the Flask server with gunicorn
# Usage: ./run.sh [port]

PORT=${1:-8080}

echo "Starting server on port $PORT..."
echo "Access at: http://localhost:$PORT"

source venv/bin/activate
gunicorn -b 0.0.0.0:$PORT main:app --access-logfile - --error-logfile -

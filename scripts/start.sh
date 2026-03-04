#!/bin/bash
echo "Starting Calculator API on port 8000..."
python3 -m uvicorn src.api:app --reload --port 8000

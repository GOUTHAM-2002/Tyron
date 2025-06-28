#!/bin/bash
# Build script for Render deployment

echo "Starting build process..."

# Update pip to latest version
python -m pip install --upgrade pip

# Install packages one by one to identify any issues
echo "Installing Flask..."
pip install Flask

echo "Installing openai..."
pip install openai

echo "Installing Pillow..."
pip install Pillow

echo "Installing Werkzeug..."
pip install Werkzeug

echo "Installing gunicorn..."
pip install gunicorn

echo "Installing requests..."
pip install requests

echo "Build completed successfully!" 
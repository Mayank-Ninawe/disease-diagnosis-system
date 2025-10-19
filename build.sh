#!/bin/bash
set -e

echo "Starting build process..."
echo "Python version:"
python --version

echo "Making build.sh executable..."
chmod +x build.sh

echo "Upgrading pip to known stable version..."
python -m pip install pip==23.1.2

echo "Installing essential build tools..."
pip install wheel==0.40.0 setuptools==65.5.1

echo "Cleaning Python environment..."
# Safe way to uninstall without breaking pip
pip freeze | grep -v "pip\|setuptools\|wheel" | xargs pip uninstall -y || true

# First install critical dependencies directly
echo "Installing critical dependencies directly..."
pip install gunicorn==20.0.4 importlib-metadata==4.13.0

# Then install Flask and other requirements
echo "Installing Flask app requirements..."
cd app
pip install -r requirements.txt

# Create necessary directories
echo "Creating necessary directories..."
cd ..
mkdir -p models
mkdir -p app/static

# Touch favicon.ico to prevent 404 errors
touch app/static/favicon.ico

# Verify installation
echo "Verifying installation..."
pip list

echo "Build completed successfully!"
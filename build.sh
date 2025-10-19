#!/bin/bash
set -e

echo "Installing latest pip..."
python -m pip install --upgrade pip

echo "Installing basic dependencies directly..."
pip install Flask==2.0.1 Flask-Cors==3.0.10 gunicorn==20.1.0 Werkzeug==2.0.1 Jinja2==3.0.1 MarkupSafe==2.0.1 itsdangerous==2.0.1 click==8.0.1

echo "Build completed successfully!"
#!/bin/bash
set -e

echo "==== Setting up deployment ===="

echo "Installing latest pip..."
python -m pip install --upgrade pip

echo "Installing basic dependencies..."
pip install Flask==2.0.1 Flask-Cors==3.0.10 gunicorn==20.1.0 Werkzeug==2.0.1 Jinja2==3.0.1 MarkupSafe==2.0.1 itsdangerous==2.0.1 click==8.0.1 requests==2.28.1 python-dotenv==0.19.2

echo "Setting up app files for deployment..."
cp app/app_deployment.py app/app.py

echo "Setup completed successfully!"
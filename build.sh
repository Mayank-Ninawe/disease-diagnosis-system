#!/bin/bash
set -e

echo "Installing latest pip..."
python -m pip install --upgrade pip

echo "Installing setuptools explicitly..."
pip install setuptools wheel

echo "Installing basic dependencies from requirements.txt..."
pip install -r requirements.txt

echo "Creating necessary directories..."
mkdir -p models

echo "Build completed successfully!"
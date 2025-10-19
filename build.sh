#!/bin/bash
set -e

echo "Installing latest pip..."
python -m pip install --upgrade pip

echo "Installing setuptools and wheel..."
pip install setuptools==69.1.0 wheel==0.42.0

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Build completed successfully!"
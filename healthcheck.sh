#!/bin/bash

echo "Health Check for Disease Diagnosis System Deployment"
echo "=================================================="

echo -e "\nChecking Python version:"
python --version

echo -e "\nChecking directory structure:"
ls -la

echo -e "\nChecking app directory:"
ls -la app

echo -e "\nChecking if app_deployment.py exists:"
if [ -f "app/app_deployment.py" ]; then
  echo "✅ app_deployment.py exists"
else
  echo "❌ app_deployment.py NOT FOUND"
fi

echo -e "\nChecking if templates directory exists:"
if [ -d "app/templates" ]; then
  echo "✅ templates directory exists"
  echo "Files in templates:"
  ls -la app/templates
else
  echo "❌ templates directory NOT FOUND"
fi

echo -e "\nChecking if static directory exists:"
if [ -d "app/static" ]; then
  echo "✅ static directory exists"
  echo "Files in static:"
  ls -la app/static
else
  echo "❌ static directory NOT FOUND"
fi

echo -e "\nChecking installed Python packages:"
pip list

echo -e "\nHealth check completed."
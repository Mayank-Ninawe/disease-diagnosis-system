"""
Entry point for the Flask application.
This script decides which version of the app to run.
"""
import os
import sys

# Get the deployment mode from environment variables
deployment_mode = os.environ.get('DEPLOYMENT_MODE', 'deployment').lower()

print(f"Starting application in {deployment_mode} mode")

if deployment_mode == 'full':
    # Try to import ML dependencies
    try:
        import numpy
        import pandas
        import sklearn
        print("ML libraries successfully imported. Starting full version.")
        
        # Run the full version with ML models
        from app.app import app
    except ImportError as e:
        print(f"Error importing ML libraries: {e}")
        print("Falling back to deployment version")
        from app.app_deployment import app
else:
    # Run the deployment version without ML dependencies
    print("Running deployment version without ML dependencies")
    from app.app_deployment import app

# This is only used when running this script directly
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
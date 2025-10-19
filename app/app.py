"""
Disease Diagnosis System - Deployment Entry Point
This file is a simple entry point that imports from app_deployment.py
"""
import os
import sys

# Print debug information
print("\n" + "="*60)
print("🏥 DISEASE DIAGNOSIS SYSTEM - ENTRY POINT")
print("="*60)
print(f"Current working directory: {os.getcwd()}")
print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")

# Check if we can import the deployment version
try:
    from app_deployment import app
    print("✅ Successfully imported app from app_deployment.py")
except ImportError as e:
    print(f"❌ Error importing from app_deployment.py: {e}")
    
    # Fall back to a very minimal Flask app if all else fails
    from flask import Flask, jsonify
    
    app = Flask(__name__)
    
    @app.route('/')
    def home():
        return jsonify({
            'status': 'Running in fallback mode',
            'error': 'Could not import app_deployment.py'
        })
        
    @app.route('/test')
    def test():
        return jsonify({
            'status': 'API is running in fallback mode',
            'error': 'Could not import app_deployment.py'
        })
    
    print("⚠️ Created fallback Flask application")

print("="*60)

if __name__ == '__main__':
    # Run the Flask app
    port = int(os.environ.get('PORT', 5000))
    print(f"🚀 Starting server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False)

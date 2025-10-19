"""
Disease Diagnosis System - Flask Backend (Deployment Version)
"""
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

print("\n" + "="*60)
print("🏥 DISEASE DIAGNOSIS SYSTEM - DEPLOYMENT VERSION")
print("="*60 + "\n")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/test', methods=['GET'])
def test():
    return jsonify({
        'status': '✅ API is running!',
        'deployment': 'successful',
        'version': '1.0.0'
    })

@app.route('/predict', methods=['POST'])
def predict():
    # This is a simplified version for initial deployment
    try:
        # Get selected symptoms from request (doesn't matter what they are for test deployment)
        data = request.get_json()
        symptoms = data.get('symptoms', [])
        
        # Just return a placeholder response for now
        return jsonify({
            'prediction': 'Deployment Test',
            'confidence': 95,
            'model_contributions': {
                'Random Forest': 33.3,
                'Naive Bayes': 33.3,
                'SVM': 33.3
            }
        })
    except Exception as e:
        print(f"Error in prediction: {str(e)}")
        return jsonify({
            'prediction': 'Error: ' + str(e),
            'confidence': 0,
            'model_contributions': {
                'Random Forest': 0,
                'Naive Bayes': 0,
                'SVM': 0
            }
        })

if __name__ == '__main__':
    print("="*60)
    print("🚀 Starting Flask Server...")
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
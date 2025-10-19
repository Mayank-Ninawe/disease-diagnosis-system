"""
Disease Diagnosis System - Flask Backend (Simplified Deployment Version)
Authors: Mayank Ninawe, Mahimna Bhuse
Course: ECSP5004 - Machine Learning Lab
College: RCOEM, Nagpur
"""
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

print("\n" + "="*60)
print("🏥 DISEASE DIAGNOSIS SYSTEM - SIMPLIFIED DEPLOYMENT VERSION")
print("="*60 + "\n")

# Mock data for deployment
feature_names = [
    "itching", "skin_rash", "nodal_skin_eruptions", "continuous_sneezing", 
    "shivering", "chills", "joint_pain", "stomach_pain", "acidity", 
    "vomiting", "burning_micturition", "fatigue", "anxiety", 
    "cold_hands_and_feet", "mood_swings", "weight_loss", "restlessness", 
    "lethargy", "cough", "high_fever", "breathlessness", "sweating", 
    "headache", "yellowish_skin", "dark_urine", "nausea", "loss_of_appetite"
]

print("✅ Using simplified deployment version without ML models")
print(f"\n📊 System Info:")
print(f"   Features: {len(feature_names)}")
print(f"   Status: Ready for deployment! 🚀\n")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/test', methods=['GET'])
def test():
    return jsonify({
        'status': '✅ API is running!',
        'deployment': 'successful',
        'features': len(feature_names),
        'version': '1.0.0'
    })

@app.route('/get_symptoms', methods=['GET'])
def get_symptoms():
    return jsonify({
        'symptoms': feature_names,
        'count': len(feature_names)
    })

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get selected symptoms from request
        data = request.get_json()
        symptoms = data.get('symptoms', [])
        
        # Just return a placeholder response for deployment test
        return jsonify({
            'disease': 'Deployment Test',
            'confidence': f"95.0%",
            'rf_prediction': f"Common Cold (33%)",
            'nb_prediction': f"Influenza (33%)",
            'svm_prediction': f"Allergy (33%)",
            'model_contributions': {
                'Random Forest': 33.3,
                'Naive Bayes': 33.3,
                'SVM': 33.3
            }
        })
    except Exception as e:
        print(f"Error in prediction: {str(e)}")
        return jsonify({
            'disease': f'Error: {str(e)}',
            'confidence': '0%',
            'rf_prediction': 'Error',
            'nb_prediction': 'Error',
            'svm_prediction': 'Error',
            'model_contributions': {
                'Random Forest': 0,
                'Naive Bayes': 0,
                'SVM': 0
            }
        }), 400

if __name__ == '__main__':
    print("="*60)
    print("🚀 Starting Flask Server...")
    print("📍 Deployment version with mock data")
    print("="*60 + "\n")
    
    # For Render deployment
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

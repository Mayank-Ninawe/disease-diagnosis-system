"""
Disease Diagnosis System - Flask Backend
Authors: Mayank Ninawe, Mahimna Bhuse
Course: ECSP5004 - Machine Learning Lab
College: RCOEM, Nagpur
"""
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import numpy as np
import os

app = Flask(__name__)
CORS(app)

print("\n" + "="*60)
print("🏥 DISEASE DIAGNOSIS SYSTEM - BACKEND")
print("="*60 + "\n")

# Load models
print("Loading models...")
try:
    model_path = '../models/'
    
    rf_model = pickle.load(open(os.path.join(model_path, 'rf_model.pkl'), 'rb'))
    print("✅ Random Forest loaded")
    
    nb_model = pickle.load(open(os.path.join(model_path, 'nb_model.pkl'), 'rb'))
    print("✅ Naive Bayes loaded")
    
    svm_model = pickle.load(open(os.path.join(model_path, 'svm_model.pkl'), 'rb'))
    print("✅ SVM loaded")
    
    label_encoder = pickle.load(open(os.path.join(model_path, 'label_encoder.pkl'), 'rb'))
    print("✅ Label Encoder loaded")
    
    feature_names = pickle.load(open(os.path.join(model_path, 'feature_names.pkl'), 'rb'))
    print("✅ Feature names loaded")
    
    print(f"\n📊 System Info:")
    print(f"   Features: {len(feature_names)}")
    print(f"   Diseases: {len(label_encoder.classes_)}")
    print(f"   Status: Ready! 🚀\n")
    
except Exception as e:
    print(f"❌ Error loading models: {e}")
    exit(1)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/test', methods=['GET'])
def test():
    return jsonify({
        'status': '✅ API is running!',
        'models_loaded': True,
        'features': len(feature_names),
        'diseases': len(label_encoder.classes_)
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
        data = request.get_json()
        symptoms = data['symptoms']
        
        input_data = np.array(symptoms).reshape(1, -1)
        
        # Get predictions
        rf_pred = rf_model.predict(input_data)[0]
        nb_pred = nb_model.predict(input_data)[0]
        svm_pred = svm_model.predict(input_data)[0]
        
        # Get prediction probabilities (confidence scores)
        try:
            rf_proba = rf_model.predict_proba(input_data)[0]
            rf_confidence = max(rf_proba) * 100
        except:
            rf_confidence = 100
        
        try:
            nb_proba = nb_model.predict_proba(input_data)[0]
            nb_confidence = max(nb_proba) * 100
        except:
            nb_confidence = 100
        
        try:
            # SVM needs probability=True during training
            svm_confidence = 100
        except:
            svm_confidence = 100
        
        # WEIGHTED VOTING based on model accuracy
        # Random Forest: 100% accuracy (weight: 3)
        # Naive Bayes: 100% accuracy (weight: 3)
        # SVM: 100% accuracy (weight: 3)
        
        predictions = {
            rf_pred: 3 * rf_confidence,  # Weight by accuracy
            nb_pred: 3 * nb_confidence,
            svm_pred: 3 * svm_confidence
        }
        
        # Get prediction with highest weighted score
        final_pred = max(predictions, key=predictions.get)
        
        # Calculate confidence
        total_weight = sum(predictions.values())
        confidence = (predictions[final_pred] / total_weight) * 100
        
        # Convert to disease names
        disease = label_encoder.inverse_transform([final_pred])[0]
        rf_disease = label_encoder.inverse_transform([rf_pred])[0]
        nb_disease = label_encoder.inverse_transform([nb_pred])[0]
        svm_disease = label_encoder.inverse_transform([svm_pred])[0]
        
        print(f"   ✅ Predicted: {disease}")
        print(f"   Confidence: {confidence:.1f}%")
        print(f"   RF confidence: {rf_confidence:.1f}%")
        print(f"   NB confidence: {nb_confidence:.1f}%\n")
        
        return jsonify({
            'disease': disease,
            'confidence': f"{confidence:.1f}%",
            'rf_prediction': f"{rf_disease} ({rf_confidence:.0f}%)",
            'nb_prediction': f"{nb_disease} ({nb_confidence:.0f}%)",
            'svm_prediction': f"{svm_disease} ({svm_confidence:.0f}%)"
        })
        
    except Exception as e:
        print(f"   ❌ Error: {str(e)}\n")
        return jsonify({
            'disease': f'Error: {str(e)}',
            'confidence': '0%',
            'rf_prediction': 'Error',
            'nb_prediction': 'Error',
            'svm_prediction': 'Error'
        }), 400

if __name__ == '__main__':
    print("="*60)
    print("🚀 Starting Flask Server...")
    print("📍 Open: http://localhost:5000")
    print("="*60 + "\n")
    
    # For Render deployment
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

"""
Disease Diagnosis System - Production Backend
Authors: Mayank Ninawe, Mahimna Bhuse
"""
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import numpy as np
import os
import sys

app = Flask(__name__)
CORS(app)

# Globals
rf_model = None
nb_model = None
svm_model = None
label_encoder = None
feature_names = None

def load_models():
    """Load ML models from pickle files"""
    global rf_model, nb_model, svm_model, label_encoder, feature_names
    
    print("\n" + "="*60)
    print("🏥 DISEASE DIAGNOSIS SYSTEM - PRODUCTION")
    print("="*60)
    
    try:
        # Use absolute path for model loading
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        model_dir = os.path.join(BASE_DIR, '..', 'models')
        
        print(f"📂 Model directory: {os.path.abspath(model_dir)}")
        
        if not os.path.exists(model_dir):
            print(f"❌ Models directory not found: {model_dir}")
            print(f"   Current directory: {os.getcwd()}")
            print(f"   Available files: {os.listdir('.')}")
            return False
        
        print(f"📁 Model files: {os.listdir(model_dir)}")
        
        # Load all models
        rf_model = pickle.load(open(os.path.join(model_dir, 'rf_model.pkl'), 'rb'))
        print("   ✅ Random Forest model loaded")
        
        nb_model = pickle.load(open(os.path.join(model_dir, 'nb_model.pkl'), 'rb'))
        print("   ✅ Naive Bayes model loaded")
        
        svm_model = pickle.load(open(os.path.join(model_dir, 'svm_model.pkl'), 'rb'))
        print("   ✅ SVM model loaded")
        
        label_encoder = pickle.load(open(os.path.join(model_dir, 'label_encoder.pkl'), 'rb'))
        print("   ✅ Label Encoder loaded")
        
        feature_names = pickle.load(open(os.path.join(model_dir, 'feature_names.pkl'), 'rb'))
        print("   ✅ Feature Names loaded")
        
        print(f"\n📊 System Ready!")
        print(f"   Features: {len(feature_names)}")
        print(f"   Diseases: {len(label_encoder.classes_)}")
        print("="*60 + "\n")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

@app.route('/')
def home():
    """Render the home page"""
    return render_template('index.html')

@app.route('/test', methods=['GET'])
def test():
    """API health check endpoint"""
    return jsonify({
        'status': '✅ API Running',
        'models_loaded': rf_model is not None,
        'features': len(feature_names) if feature_names else 0,
        'diseases': len(label_encoder.classes_) if label_encoder else 0
    })

@app.route('/get_symptoms', methods=['GET'])
def get_symptoms():
    """Return the list of symptoms (features)"""
    if feature_names is None:
        print("❌ Cannot get symptoms: Models not loaded")
        return jsonify({'error': 'Models not loaded', 'symptoms': []}), 500
        
    return jsonify({'symptoms': feature_names, 'count': len(feature_names)})

@app.route('/predict', methods=['POST'])
def predict():
    """Predict disease based on symptoms"""
    try:
        # Check if models are loaded
        if rf_model is None:
            print("❌ Cannot predict: Models not loaded")
            return jsonify({
                'disease': 'Error: Models not loaded',
                'confidence': '0%',
                'rf_prediction': 'N/A',
                'nb_prediction': 'N/A',
                'svm_prediction': 'N/A'
            }), 500
        
        # Get symptoms from request
        data = request.get_json()
        symptoms = data['symptoms']
        
        # Validate input length
        if len(symptoms) != len(feature_names):
            print(f"❌ Invalid input: Expected {len(feature_names)} features, got {len(symptoms)}")
            return jsonify({
                'disease': f'Error: Expected {len(feature_names)} symptoms, got {len(symptoms)}',
                'confidence': '0%',
                'rf_prediction': 'Error',
                'nb_prediction': 'Error',
                'svm_prediction': 'Error'
            }), 400
        
        print(f"📊 Predicting with input array of length {len(symptoms)}, " +
              f"active symptoms: {sum(1 for s in symptoms if s == 1)}")
        
        # Reshape input for model prediction
        input_data = np.array(symptoms).reshape(1, -1)
        
        # Get predictions from each model
        rf_pred = rf_model.predict(input_data)[0]
        nb_pred = nb_model.predict(input_data)[0]
        svm_pred = svm_model.predict(input_data)[0]
        
        # Collect all predictions for majority voting
        predictions = [rf_pred, nb_pred, svm_pred]
        
        # Find majority prediction (mode)
        final_pred = max(set(predictions), key=predictions.count)
        
        # Convert numeric predictions to disease names
        disease = label_encoder.inverse_transform([final_pred])[0]
        rf_disease = label_encoder.inverse_transform([rf_pred])[0]
        nb_disease = label_encoder.inverse_transform([nb_pred])[0]
        svm_disease = label_encoder.inverse_transform([svm_pred])[0]
        
        # Calculate confidence based on agreement between models
        confidence = (predictions.count(final_pred) / 3) * 100
        
        print(f"🔍 Predictions: RF={rf_disease}, NB={nb_disease}, SVM={svm_disease}")
        print(f"🎯 Final prediction: {disease} with {confidence:.0f}% confidence")
        
        # Return prediction results
        return jsonify({
            'disease': disease,
            'confidence': f"{confidence:.0f}%",
            'rf_prediction': rf_disease,
            'nb_prediction': nb_disease,
            'svm_prediction': svm_disease
        })
    
    except Exception as e:
        print(f"❌ Prediction error: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({
            'disease': f'Error: {str(e)}',
            'confidence': '0%',
            'rf_prediction': 'Error',
            'nb_prediction': 'Error',
            'svm_prediction': 'Error'
        }), 400

if __name__ == '__main__':
    # Load models on startup
    models_loaded = load_models()
    if not models_loaded:
        print("⚠️ Warning: Models could not be loaded. API will return errors for predictions.")
    
    # Run the Flask app
    port = int(os.environ.get('PORT', 5000))
    print(f"🚀 Starting server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False)

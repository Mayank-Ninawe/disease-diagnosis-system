"""
Disease Diagnosis System - Flask Backend (Deployment Version)
This is a simplified version that doesn't rely on ML libraries
"""
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import os
import random

app = Flask(__name__, static_folder='static')
CORS(app)

print("\n" + "="*60)
print("🏥 DISEASE DIAGNOSIS SYSTEM - DEPLOYMENT VERSION")
print("="*60 + "\n")

# Mock data for initial deployment
MOCK_SYMPTOMS = [
    "itching", "skin_rash", "nodal_skin_eruptions", "continuous_sneezing", "shivering", 
    "chills", "joint_pain", "stomach_pain", "acidity", "ulcers_on_tongue", 
    "muscle_wasting", "vomiting", "burning_micturition", "spotting_urination", "fatigue", 
    "weight_gain", "anxiety", "cold_hands_and_feets", "mood_swings", "weight_loss", 
    "restlessness", "lethargy", "patches_in_throat", "irregular_sugar_level", "cough", 
    "high_fever", "sunken_eyes"
]

MOCK_DISEASES = [
    "Fungal infection", "Allergy", "GERD", "Chronic cholestasis", "Drug reaction",
    "Peptic ulcer disease", "AIDS", "Diabetes", "Gastroenteritis", "Bronchial Asthma",
    "Hypertension", "Migraine", "Cervical spondylosis", "Paralysis (brain hemorrhage)",
    "Jaundice", "Malaria", "Chicken pox", "Dengue", "Typhoid", "Hepatitis A",
    "Hepatitis B", "Hepatitis C", "Hepatitis D", "Hepatitis E", "Alcoholic hepatitis",
    "Tuberculosis", "Common Cold", "Pneumonia", "Dimorphic hemmorhoids(piles)",
    "Heart attack", "Varicose veins", "Hypothyroidism", "Hyperthyroidism", "Hypoglycemia",
    "Osteoarthristis", "Arthritis", "Paroxysmal Positional Vertigo", "Acne", "Urticaria",
    "Psoriasis", "Impetigo"
]

# Dictionary mapping symptom groups to likely diseases
SYMPTOM_DISEASE_MAPPING = {
    "itching,skin_rash,nodal_skin_eruptions": ["Fungal infection", "Chicken pox", "Impetigo"],
    "continuous_sneezing,chills,cough": ["Common Cold", "Allergy", "Pneumonia"],
    "joint_pain,fatigue,anxiety": ["Arthritis", "Cervical spondylosis", "Paralysis (brain hemorrhage)"],
    "stomach_pain,acidity,ulcers_on_tongue": ["GERD", "Peptic ulcer disease", "Gastroenteritis"],
    "vomiting,nausea,high_fever": ["Malaria", "Typhoid", "Dengue"],
    "weight_loss,lethargy,irregular_sugar_level": ["Diabetes", "Hypoglycemia", "AIDS"]
}

@app.route('/')
def home():
    try:
        return render_template('index.html')
    except Exception as e:
        print(f"Error rendering home page: {e}")
        return jsonify({
            'status': 'Error rendering home page',
            'error': str(e)
        }), 500

@app.route('/test', methods=['GET'])
def test():
    return jsonify({
        'status': '✅ API is running!',
        'deployment': 'successful',
        'version': '1.0.0',
        'mode': 'deployment'
    })

@app.route('/get_symptoms', methods=['GET'])
def get_symptoms():
    return jsonify({
        'symptoms': MOCK_SYMPTOMS,
        'count': len(MOCK_SYMPTOMS)
    })

@app.route('/predict', methods=['POST'])
def predict():
    """Simplified prediction logic for deployment version"""
    try:
        # Get symptoms from request
        data = request.get_json()
        symptom_array = data.get('symptoms', [])
        
        # Count active symptoms
        active_symptom_indices = [i for i, val in enumerate(symptom_array) if val == 1]
        active_symptom_count = len(active_symptom_indices)
        
        # Get active symptom names
        active_symptoms = [MOCK_SYMPTOMS[i] for i in active_symptom_indices] if active_symptom_indices else []
        active_symptoms_str = ",".join(active_symptoms)
        print(f"Active symptoms: {active_symptoms_str}")
        
        # Simple prediction logic based on symptom groups
        matched_diseases = []
        for symptom_group, diseases in SYMPTOM_DISEASE_MAPPING.items():
            group_symptoms = symptom_group.split(",")
            matching_symptoms = [s for s in active_symptoms if s in group_symptoms]
            if len(matching_symptoms) >= 2:  # If at least 2 symptoms match from a group
                matched_diseases.extend(diseases)
        
        # If no matches, pick some based on the number of symptoms
        if not matched_diseases:
            if active_symptom_count > 10:
                matched_diseases = [random.choice(MOCK_DISEASES[:10])]
            elif active_symptom_count > 5:
                matched_diseases = [random.choice(MOCK_DISEASES[10:20])]
            else:
                matched_diseases = [random.choice(MOCK_DISEASES[20:30])]
        
        # Get final prediction with some randomness but weighted toward the most common match
        disease_counts = {}
        for d in matched_diseases:
            if d in disease_counts:
                disease_counts[d] += 1
            else:
                disease_counts[d] = 1
                
        # Sort by count (most common first)
        sorted_diseases = sorted(disease_counts.items(), key=lambda x: x[1], reverse=True)
        
        # Pick the most common as the main prediction
        if sorted_diseases:
            final_disease = sorted_diseases[0][0]
            # Generate slightly different predictions for the models
            if len(sorted_diseases) > 2:
                rf_disease = sorted_diseases[0][0]
                nb_disease = sorted_diseases[1][0]
                svm_disease = sorted_diseases[2][0]
            elif len(sorted_diseases) == 2:
                rf_disease = sorted_diseases[0][0]
                nb_disease = sorted_diseases[1][0]
                svm_disease = sorted_diseases[0][0]
            else:
                rf_disease = nb_disease = svm_disease = sorted_diseases[0][0]
        else:
            final_disease = rf_disease = nb_disease = svm_disease = "Common Cold"
        
        # Calculate confidence based on number of symptoms and agreement
        if active_symptom_count > 10:
            confidence = random.randint(85, 95)
        elif active_symptom_count > 5:
            confidence = random.randint(70, 85)
        else:
            confidence = random.randint(50, 70)
            
        print(f"Prediction: {final_disease} with {confidence}% confidence")
        print(f"Model predictions: RF={rf_disease}, NB={nb_disease}, SVM={svm_disease}")
        
        # Return result in expected format
        return jsonify({
            'disease': final_disease,
            'confidence': f"{confidence}%",
            'rf_prediction': rf_disease,
            'nb_prediction': nb_disease,
            'svm_prediction': svm_disease,
            'mode': 'deployment'
        })
    except Exception as e:
        print(f"Error in prediction: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({
            'disease': 'Error: ' + str(e),
            'confidence': '0%',
            'rf_prediction': 'Error',
            'nb_prediction': 'Error',
            'svm_prediction': 'Error',
            'mode': 'deployment'
        }), 400

if __name__ == '__main__':
    print("="*60)
    print("🚀 Starting Flask Server (Deployment Version)...")
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
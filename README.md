# 🏥 Intelligent Disease Diagnosis System

An AI-powered healthcare application that predicts diseases from patient symptoms using ensemble machine learning techniques.

## 👥 Team Members

**Group ID:** Group_XX_ML_Lab_V_A  
**Course:** ECSP5004 - Machine Learning Lab  
**College:** Shri Ramdeobaba College of Engineering and Management, Nagpur  
**Academic Year:** 2025-26

| Name | Roll Number | Contribution |
|------|-------------|--------------|
| Mayank Ninawe | XXX | Data preprocessing, Model training, Evaluation |
| Mahimna Bhuse | YYY | Backend development, Frontend design, Integration |

---

## 📖 Project Description

This project implements a web-based disease diagnosis system that uses machine learning to predict diseases based on patient-reported symptoms. The system employs an ensemble of three ML algorithms (Random Forest, Naive Bayes, and SVM) to achieve high prediction accuracy.

### Key Highlights
- ✅ 130 symptoms covering 41 different diseases
- ✅ 100% model accuracy on test data
- ✅ Real-time predictions via web interface
- ✅ Ensemble learning for robust predictions
- ✅ User-friendly symptom selection interface

---

## 🚀 Features

### Core Features
1. **Multi-Symptom Selection**: Select multiple symptoms from a comprehensive list of 130 medical symptoms
2. **Ensemble Prediction**: Uses 3 ML algorithms with majority voting for robust results
3. **Confidence Score**: Displays prediction confidence based on model agreement
4. **Individual Model Predictions**: Shows what each model predicted separately
5. **Web-Based GUI**: Clean, responsive interface built with Bootstrap 5
6. **Real-Time Processing**: Instant predictions with visual feedback

### Technical Features
- Binary symptom encoding (0/1)
- Feature validation and error handling
- RESTful API architecture
- Cross-Origin Resource Sharing (CORS) support
- Pickle-based model persistence

---

## 💻 Technology Stack

### Backend
- **Language**: Python 3.10
- **Framework**: Flask 2.3.0
- **ML Libraries**: 
  - scikit-learn 1.3.0
  - pandas 2.0.0
  - numpy 1.24.0
- **Model Serialization**: pickle

### Frontend
- HTML5
- CSS3 (Bootstrap 5.1.3)
- Vanilla JavaScript
- Responsive design

### Machine Learning
- **Algorithms**: Random Forest, Gaussian Naive Bayes, SVM
- **Technique**: Ensemble Learning (Majority Voting)
- **Encoding**: Label Encoding for target variable

---

## 📊 Dataset Information

| Attribute | Value |
|-----------|-------|
| **Source** | Kaggle Disease Symptom Prediction |
| **Total Records** | 4,920 |
| **Features** | 130 symptoms |
| **Target Classes** | 41 diseases |
| **Feature Type** | Binary (0/1) |
| **Split Ratio** | 80% Train, 20% Test |

### Sample Diseases Covered
- Malaria, Dengue, Typhoid
- Diabetes, Hypertension
- Common Cold, Pneumonia
- Paralysis (Brain Hemorrhage)
- Heart Attack, Migraine
- And 31 more...

---

## 📁 Project Structure

disease-diagnosis/
│
├── README.md # Project documentation
├── requirements.txt # Python dependencies
│
├── data/
│ └── Training.csv # Disease-symptom dataset
│
├── notebooks/
│ ├── 01_data_exploration.ipynb # EDA notebook
│ └── 02_model_training.ipynb # Model training notebook
│
├── models/
│ ├── rf_model.pkl # Random Forest model
│ ├── nb_model.pkl # Naive Bayes model
│ ├── svm_model.pkl # SVM model
│ ├── label_encoder.pkl # Disease label encoder
│ └── feature_names.pkl # Symptom feature names
│
├── app/
│ ├── app.py # Flask backend server
│ └── templates/
│ └── index.html # Frontend interface
│
└── screenshots/
├── homepage.png
├── symptom_selection.png
└── prediction_result.png

text

---

## 🔧 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Web browser (Chrome, Firefox, Edge)

### Step 1: Extract Project
unzip Group_XX_ML_Lab_V_A.zip
cd Group_XX_ML_Lab_V_A

text

### Step 2: Install Dependencies
pip install -r requirements.txt

text

### Step 3: Verify Models (Optional)
jupyter notebook

Open and run notebooks/02_model_training.ipynb
text

### Step 4: Start Flask Server
cd app
python app.py

text

### Step 5: Access Application
Open browser and navigate to:
http://localhost:5000

text

---

## 📖 Usage Instructions

### Making a Prediction

1. **Select Symptoms**: 
   - Hold `Ctrl` (Windows) or `Cmd` (Mac)
   - Click to select 3-5 symptoms you're experiencing

2. **Click Predict**: 
   - Press the "🔍 Predict Disease" button

3. **View Results**:
   - See predicted disease name
   - Check confidence score
   - Review individual model predictions

### Example Test Case

**Symptoms**: High Fever + Headache + Vomiting + Chills  
**Expected Result**: Malaria (100% confidence)

---

## 📈 Model Performance

### Training Results

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| **Random Forest** | 100.00% | 100.00% | 100.00% | 100.00% |
| **Naive Bayes** | 100.00% | 100.00% | 100.00% | 100.00% |
| **SVM** | 100.00% | 100.00% | 100.00% | 100.00% |
| **Ensemble** | 100.00% | 100.00% | 100.00% | 100.00% |

### Confidence Score Interpretation

- **100%**: All 3 models agree (Most reliable)
- **67%**: 2 out of 3 models agree (Reliable)
- **33%**: Only 1 model agrees (Less reliable - need more symptoms)

---

## 🧪 Testing

### API Testing

**Health Check:**
curl http://localhost:5000/test

text

**Get Symptoms:**
curl http://localhost:5000/get_symptoms

text

**Make Prediction:**
curl -X POST http://localhost:5000/predict
-H "Content-Type: application/json"
-d '{"symptoms": [1,0,0,1,0,...]}' # 130 binary values

text

---

## 🔮 Future Enhancements

### Planned Features
- [ ] Mobile application (Android/iOS)
- [ ] Integration with hospital management systems
- [ ] Support for 100+ diseases and 200+ symptoms
- [ ] Image-based diagnosis (X-ray, CT scan analysis)
- [ ] Multi-language support (Hindi, Marathi, etc.)
- [ ] Telemedicine consultation integration
- [ ] Patient history tracking
- [ ] PDF report generation

### Technical Improvements
- [ ] Deep learning models (CNN, LSTM)
- [ ] Cloud deployment (AWS, Azure, Heroku)
- [ ] Database integration (PostgreSQL, MongoDB)
- [ ] User authentication system
- [ ] RESTful API documentation (Swagger)

---

## ⚠️ Disclaimer

This is an **educational AI tool** developed for academic purposes. It is **NOT a substitute** for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for medical concerns.

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

Educational Project © 2025 - RCOEM, Nagpur

---

## 📞 Contact

**Project Developers:**

**Mayank Ninawe**  
📧 Email: [your-email]  
🔗 LinkedIn: [your-profile]

**Mahimna Bhuse**  
📧 Email: [your-email]  
🔗 LinkedIn: [your-profile]

**Guide:**  
[Professor Name]  
Department of Electronics Engineering  
RCOEM, Nagpur

---

## 🙏 Acknowledgements

- Our guide [Professor Name] for valuable guidance
- Department of Electronics Engineering, RCOEM
- Kaggle for providing the dataset
- scikit-learn community for excellent ML libraries

---

**Made with ❤️ by Mayank & Mahimna**

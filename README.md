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
- **Language**: Python 3.13.4
- **Framework**: Flask 2.0.1
- **ML Libraries**: 
  - scikit-learn 1.3.0
  - pandas 2.0.0
  - numpy 1.24.0
- **Model Serialization**: pickle
- **Deployment**: Render Cloud Platform

### Frontend
- HTML5
- CSS3 (Bootstrap 5.1.3)
- Vanilla JavaScript
- Responsive design with animation effects
- Mobile-friendly interface

### Machine Learning
- **Algorithms**: Random Forest, Gaussian Naive Bayes, SVM
- **Technique**: Enhanced Ensemble Learning (Weighted Voting based on confidence scores)
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

```
disease-diagnosis/
│
├── README.md                  # Project documentation
├── requirements.txt           # Python dependencies
├── runtime.txt                # Python version specification
├── Procfile                   # Deployment process file
├── render.yaml                # Render deployment configuration
│
├── data/
│   ├── Training.csv           # Disease-symptom dataset
│   └── Testing.csv            # Test dataset
│
├── notebooks/
│   ├── 01_data_exploration.ipynb  # EDA notebook
│   └── 02_model_training.ipynb    # Model training notebook
│
├── models/
│   ├── rf_model.pkl           # Random Forest model
│   ├── nb_model.pkl           # Naive Bayes model
│   ├── svm_model.pkl          # SVM model
│   ├── label_encoder.pkl      # Disease label encoder
│   └── feature_names.pkl      # Symptom feature names
│
├── app/
│   ├── app.py                 # Flask backend server with ML integration
│   ├── app_deployment.py      # Simplified deployment version
│   └── templates/
│       └── index.html         # Enhanced frontend interface
│
└── screenshots/
    ├── homepage.png
    ├── symptom_selection.png
    └── prediction_result.png
```

---

## 🔧 Installation & Setup

### Prerequisites
- Python 3.10 or higher (3.13.4 recommended)
- pip package manager
- Web browser (Chrome, Firefox, Edge)

### Local Development Setup

#### Step 1: Clone the Repository
```bash
git clone https://github.com/Mayank-Ninawe/disease-diagnosis-system.git
cd disease-diagnosis-system
```

#### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

#### Step 3: Verify Models (Optional)
```bash
jupyter notebook
```
Open and run `notebooks/02_model_training.ipynb` to train models from scratch

#### Step 4: Start Flask Server
```bash
cd app
python app.py
```

#### Step 5: Access Application
Open browser and navigate to:
```
http://localhost:5000
```

## 🚀 Deployment Guide

### Render.com Deployment

This application uses a two-phase deployment strategy on [Render.com](https://render.com/):

1. **Phase 1 (Current)**: Simplified version without ML dependencies to avoid build errors
2. **Phase 2**: Full application with ML capabilities once base deployment is stable

#### Key Deployment Files

| File | Purpose |
|------|---------|
| `wsgi.py` | Entry point that chooses between full/simplified versions |
| `Procfile` | Defines web process using gunicorn with wsgi.py |
| `requirements.txt` | Core dependencies (ML dependencies commented out) |
| `build.sh` | Custom build script that installs setuptools explicitly |
| `app/app.py` | Full version with ML functionality |
| `app/app_deployment.py` | Simplified version without ML dependencies |

#### Step-by-Step Deployment Instructions

1. **Prepare Your Codebase**
   - Ensure all files are committed to your repository
   - Make sure `wsgi.py` and `build.sh` are in the root directory
   - Verify `requirements.txt` has ML dependencies commented out initially

2. **Create Render Account**
   - Sign up at [Render.com](https://render.com/)
   - Verify your email address

3. **Connect Repository**
   - Go to Render Dashboard
   - Click "New +" and select "Web Service"
   - Connect your GitHub/GitLab account
   - Select the disease-diagnosis repository

4. **Configure Web Service**
   - **Name**: `disease-diagnosis` (or your preferred name)
   - **Environment**: `Python 3`
   - **Region**: Choose nearest data center
   - **Branch**: `main` (or your deployment branch)
   - **Build Command**: `chmod +x build.sh && ./build.sh`
   - **Start Command**: `gunicorn wsgi:app`
   - **Plan**: Free (or paid if needed)

5. **Add Environment Variables**
   - Click "Advanced" during setup
   - Add: `PYTHON_VERSION=3.13.4`
   - Add: `DEPLOYMENT_MODE=deployment`

6. **Deploy the Service**
   - Click "Create Web Service"
   - Wait for build and deployment (5-10 minutes)
   - Your app will be available at: `https://your-service-name.onrender.com`

### Troubleshooting Common Issues

| Issue | Solution |
|-------|----------|
| **setuptools.build_meta errors** | Our `build.sh` now explicitly installs setuptools first |
| **numpy build failures** | ML dependencies are commented out in `requirements.txt` for initial deployment |
| **Module Not Found** | Check if setuptools is installed properly |
| **Application Error** | Verify `wsgi.py` is properly detecting deployment mode |
| **Timeout During Build** | Increase build timeout in Render settings |

### Upgrading to Full ML Functionality

After your simplified version is successfully deployed:

1. **Update requirements.txt gradually**:
   ```bash
   # First add numpy alone and test
   numpy==1.24.0
   
   # Then add scikit-learn and test
   scikit-learn==1.3.0
   
   # Finally add pandas
   pandas==2.0.0
   ```

2. **Upload ML model files**:
   - Create a `/models` directory in your repository
   - Upload the pickle model files to this directory
   - Commit and push these changes

3. **Switch to full mode**:
   - In Render dashboard, change the environment variable:
   ```
   DEPLOYMENT_MODE=full
   ```

4. **Redeploy your application**:
   - Manually trigger a redeploy from the Render dashboard
   - Monitor logs to ensure models are loaded correctly

### Monitoring & Debugging

- **View Logs**: Access detailed logs from Render Dashboard
- **Error Tracking**: Check application logs for model loading errors
- **Memory Usage**: Monitor RAM usage and upgrade plan if needed
- **Request Tracing**: Enable request logging to diagnose API issues

**Pro Tip**: If you encounter persistent ML dependency issues, consider using precompiled wheels or Docker deployment.

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

#### Local Testing

```bash
# Health Check
curl http://localhost:5000/test

# Get Symptoms List
curl http://localhost:5000/get_symptoms

# Make Prediction (Local)
curl -X POST http://localhost:5000/predict \
-H "Content-Type: application/json" \
-d '{"symptoms": [1,0,0,1,0,...]}' # 130 binary values
```

#### Cloud Testing (Render)

```bash
# Replace with your actual Render URL
export RENDER_URL=https://your-app-name.onrender.com

# Health Check
curl $RENDER_URL/test

# Get Symptoms List
curl $RENDER_URL/get_symptoms

# Make Prediction
curl -X POST $RENDER_URL/predict \
-H "Content-Type: application/json" \
-d '{"symptoms": [1,0,0,1,0,...]}' # 130 binary values
```

> **Note**: The simplified deployment version returns mock predictions until ML functionality is added back.

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
- [x] Cloud deployment (Render.com)
- [ ] Dockerization for consistent environment
- [ ] Deep learning models (CNN, LSTM)
- [ ] Database integration (PostgreSQL, MongoDB)
- [ ] User authentication system
- [ ] RESTful API documentation (Swagger)
- [ ] CI/CD pipeline integration

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

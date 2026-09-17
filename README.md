# 🫀 CardioInsight

<p align="center">

  <strong>AI-Powered Heart Disease Prediction & Clinical Decision Support</strong>

</p>

<p align="center">

  A Machine Learning project that analyzes patient health, clinical, and lifestyle data to predict the likelihood of heart disease.

</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)

![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi)

![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?logo=streamlit)

![Scikit--learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?logo=scikitlearn)

![Status](https://img.shields.io/badge/Status-Completed-success)

</p>

---

## 📌 About The Project

****CardioInsight**** is a Machine Learning-based application developed to provide a prediction of heart disease based on a set of patient characteristics.

The project covers the complete Machine Learning workflow:

****Data Collection → Data Cleaning → EDA → Feature Engineering → Preprocessing → Model Training → Model Evaluation → API → Interactive Web Application****

The system uses ****FastAPI**** as the backend prediction API and ****Streamlit**** as the interactive frontend.

> ⚠️ ****Medical Disclaimer:**** CardioInsight is an educational and research project. Its predictions are not a medical diagnosis and should not replace consultation with a qualified healthcare professional.

---

## ✨ Features

- 🫀 Heart disease prediction.

- 📊 Exploratory Data Analysis.

- 🧹 Data cleaning and preprocessing.

- 🧠 Training and comparison of multiple ML algorithms.

- 📐 Feature engineering using BMI and Pulse Pressure.

- 🔢 Numerical feature scaling.

- 🏷️ Ordinal and One-Hot Encoding.

- 🤖 SVM-based prediction model.

- 📈 Heart disease probability estimation.

- ⚡ FastAPI REST API.

- 🖥️ Interactive Streamlit interface.

- 📦 Serialized trained model using Joblib.

---

## 📂 Dataset

The project uses a ****synthetic heart disease dataset****.

### Original Dataset

- ****50,000 records****

- ****21 original features****

The dataset contains information related to:

- Demographics

- Medical history

- Blood pressure

- Heart rate

- Blood sugar

- Cholesterol

- Lifestyle

- Smoking

- Alcohol intake

- Physical activity

- Diet

- Stress level

### Target Variable

The target column is:

```text

Heart_Disease

```
 Value | Meaning          
 ----  | ---------------- 

 | `0` | No Heart Disease |

 | `1` | Heart Disease    |

After cleaning and feature engineering:

```text

47,765 rows

22 columns

```

---

# 🔬 Data Preprocessing

## 🧹 Data Cleaning

Missing values in `Alcohol_Intake` were handled by replacing them with:

```text

None

```

Invalid blood pressure records were removed:

```python

df = df[df['Systolic_BP'] > df['Diastolic_BP']]

```

---

## 🧮 Feature Engineering

### BMI

BMI is calculated automatically from weight and height:

```text

BMI = Weight / (Height / 100)²

```

### Pulse Pressure

Pulse Pressure is calculated from systolic and diastolic blood pressure:

```text

Pulse_Pressure = Systolic_BP - Diastolic_BP

```

These features are calculated automatically by the application and do not need to be entered manually by the user.

---

## 🔤 Feature Encoding

### Numerical Features

```text

Age

Weight

Height

BMI

Systolic_BP

Diastolic_BP

Pulse_Pressure

Heart_Rate

Blood_Sugar_Fasting

Cholesterol_Total

```

Numerical features are scaled using:

```text

StandardScaler

```

### Ordinal Features

```text

Diet

Stress_Level

Physical_Activity

```

These features are encoded using:

```text

OrdinalEncoder

```

### Nominal Features

```text

Gender

Smoking

Alcohol_Intake

```

These features are transformed using One-Hot Encoding.

---

# 🤖 Machine Learning

Several classification algorithms were trained and evaluated:

- 🌳 Decision Tree

- ⚡ XGBoost

- 🚀 AdaBoost

- 📈 Gradient Boosting

- 🌲 Random Forest

- 🎯 SVM (RBF)

- 📊 Logistic Regression

- 🧮 Naive Bayes

- 📍 KNN

The dataset was split into:

```text

80% Training

20% Testing

```

using stratification.

---

# 📊 Model Performance

| Model               |   Train Accuracy |    Test Accuracy |          ROC-AUC |           Recall |        Precision |         F1-Score |

| ------------------- | ---------------: | ---------------: | ---------------: | ---------------: | ---------------: | ---------------: |

| Decision Tree       |             100% |             100% |           1.0000 |           1.0000 |           1.0000 |           1.0000 |

| XGBoost             |             100% |             100% |           1.0000 |           1.0000 |           1.0000 |           1.0000 |

| AdaBoost            |             100% |             100% |           1.0000 |           1.0000 |           1.0000 |           1.0000 |

| Gradient Boosting   |             100% |             100% |           1.0000 |           1.0000 |           1.0000 |           1.0000 |

| Random Forest       |             100% |             100% |           1.0000 |           1.0000 |           1.0000 |           1.0000 |

| ****SVM (RBF)**** | ****98.63%**** | ****96.20%**** | ****0.9946**** | ****96.04%**** | ****95.76%**** | ****95.90%**** |

| Logistic Regression |           92.49% |           92.52% |           0.9830 |           92.31% |           91.58% |           91.95% |

| Naive Bayes         |           83.45% |           83.59% |           0.9232 |           79.35% |           84.27% |           81.73% |

| KNN                 |           85.38% |           83.22% |           0.9405 |           68.79% |           93.17% |           79.14% |

### Final Application Model

The application uses:

```python

SVC(

    C=10,

    kernel='rbf',

    probability=True,

    random_state=42

)

```

### SVM Results

```text

Training Accuracy : 98.63%

Testing Accuracy  : 96.20%

ROC-AUC            : 0.9946

Recall             : 96.04%

Precision          : 95.76%

F1-Score           : 95.90%

```

---

# 🏗️ Project Architecture

```text

                         ┌─────────────────────┐

                         │  Streamlit Frontend  │

                         └──────────┬──────────┘

                                    │

                                    │ POST Request

                                    ▼

                         ┌─────────────────────┐

                         │    FastAPI Backend   │

                         └──────────┬──────────┘

                                    │

                                    ▼

                         ┌─────────────────────┐

                         │   Preprocessing      │

                         │                     │

                         │ BMI                 │

                         │ Pulse Pressure      │

                         │ Encoding            │

                         │ Scaling             │

                         └──────────┬──────────┘

                                    │

                                    ▼

                         ┌─────────────────────┐

                         │     SVM Model       │

                         │       (RBF)         │

                         └──────────┬──────────┘

                                    │

                                    ▼

                         ┌─────────────────────┐

                         │ Prediction +         │

                         │ Probability          │

                         └─────────────────────┘

```

---

# 📁 Project Structure

```text

CardioInsight/

│

├── 📁 Data/

│   ├── 📁 origin/

│   │   └── synthetic_heart_disease_dataset.csv

│   │

│   └── 📁 processed/

│       └── synthetic_heart_disease_cleaned.csv

├── requirements.txt

├── README.md

└── Copy_of_CardioInsight_Combined.ipynb              ( Full Project)

```

---

# 🛠️ Technologies

| Technology          | Purpose                   |

| ------------------- | ------------------------- |

| 🐍 Python           | Main programming language |

| 🐼 Pandas           | Data manipulation         |

| 🔢 NumPy            | Numerical computing       |

| 🤖 Scikit-learn     | Machine Learning          |

| ⚡ XGBoost          | Gradient boosting model   |

| 📦 Joblib           | Model serialization       |

| 🚀 FastAPI          | Backend REST API          |

| 🖥️ Streamlit      | Interactive web interface |

| 🔬 Jupyter Notebook | EDA & experiments         |

| 💻 VS Code          | Development               |

| 🌐 Git & GitHub     | Version control           |

---

# 🚀 How To Use

CardioInsight is designed to be run through **Google Colab**.

The repository only requires the following project files:

```text
CardioInsight/
│
├── 📓 Copy_of_CardioInsight_Combined.ipynb
├── 📊 CardioInsight_Presentation.pptx
└── 📖 README.md
```

The complete application, model training workflow, FastAPI backend, Streamlit interface, and temporary deployment files are created and executed inside the Google Colab environment.

---

# 📓 Running the Project with Google Colab

The complete CardioInsight project is contained in:

```text
Copy_of_CardioInsight_Combined.ipynb
```

Upload this notebook to **Google Colab** and run the cells in order.

The notebook includes:

```text
Data Loading
    ↓
Data Cleaning
    ↓
Exploratory Data Analysis
    ↓
Feature Engineering
    ↓
Data Preprocessing
    ↓
Model Training
    ↓
Model Comparison
    ↓
SVM Selection
    ↓
Model Serialization
    ↓
FastAPI API
    ↓
Streamlit Interface
    ↓
ngrok Live Demo
```

## 1️⃣ Open the Notebook

Open **Google Colab** and upload:

```text
Copy_of_CardioInsight_Combined.ipynb
```

Run the notebook cells from top to bottom.

## 2️⃣ Install Dependencies

The notebook installs the required deployment packages:

```python
!pip install -q streamlit fastapi uvicorn pyngrok joblib
```

The notebook also contains the dependencies required for the Machine Learning and data-analysis workflow.

## 3️⃣ Create the Model Artifact

After training and selecting the SVM (RBF) model, the notebook creates:

```text
cardio_model.pkl
```

The artifact contains the trained model and the preprocessing components required for prediction.

The notebook then creates the temporary deployment files:

```text
api.py
app.py
```

These files are generated inside the Colab session only.

## 4️⃣ Run FastAPI

FastAPI is started inside Colab on port `8000`:

```python
!pkill -f uvicorn
!uvicorn api:app --host 0.0.0.0 --port 8000 > api.log 2>&1 &
```

## 5️⃣ Create the FastAPI ngrok Tunnel

Configure your own ngrok authentication token:

```python
!ngrok config add-authtoken "YOUR_NGROK_AUTHTOKEN"
```

**Do not upload your real ngrok token to GitHub.**

Then create the public API tunnel:

```python
from pyngrok import ngrok

ngrok.kill()

api_tunnel = ngrok.connect(8000)

API_URL = api_tunnel.public_url

print("API URL:")
print(API_URL)
```

## 6️⃣ Run Streamlit

Start the Streamlit interface on port `8501`:

```python
!pkill -f streamlit
!streamlit run app.py --server.port 8501 --server.address 0.0.0.0 > streamlit.log 2>&1 &
```

Then expose it using ngrok:

```python
import time

time.sleep(3)

!cat streamlit.log

streamlit_tunnel = ngrok.connect(8501)

print("Open your CardioInsight app:")
print(streamlit_tunnel.public_url)
```

Open the generated public URL to access the CardioInsight interface.

### ⚠️ Important

When running CardioInsight through **Google Colab + ngrok**, the Colab session must remain active because the FastAPI and Streamlit servers are running inside the Colab environment.

The ngrok URLs are temporary and may change when a new tunnel is created.

No local FastAPI or Streamlit setup is required. The deployment files generated by the notebook are temporary and remain inside the Colab session.

---

# 🧑‍⚕️ Using CardioInsight

The user enters patient information through the Streamlit interface.

### 👤 Patient Information

- Age

- Weight

- Height

- Gender

- Smoking

### 🏥 Medical History

- Hypertension

- Diabetes

- Hyperlipidemia

- Family History

- Previous Heart Attack

### ❤️ Clinical Measurements

- Systolic Blood Pressure

- Diastolic Blood Pressure

- Heart Rate

- Fasting Blood Sugar

- Total Cholesterol

### 🥗 Lifestyle

- Physical Activity

- Diet

- Stress Level

- Alcohol Intake

After submitting the information, the application sends the data to the FastAPI backend.

The backend:

```text

Receives Patient Data

        ↓

Calculates BMI

        ↓

Calculates Pulse Pressure

        ↓

Encodes Categorical Features

        ↓

Scales Numerical Features

        ↓

Loads SVM Model

        ↓

Generates Prediction

        ↓

Calculates Probability

```

The result is then displayed in the Streamlit interface.

---

# 🔌 API

## POST `/predict`

The endpoint receives patient data and returns the prediction.

### Example Response

```json

{

    "prediction": 1,

    "probability": 0.9889

}

```

### Prediction Meaning

```text

0 → No Heart Disease

1 → Heart Disease

```

The `probability` represents the model's estimated probability for the ****Heart Disease**** class.

---

# 🔄 Complete Workflow

```text

              Patient

                 │

                 ▼

        Streamlit Interface

                 │

                 ▼

          Patient Inputs

                 │

                 ▼

            FastAPI API

                 │

                 ▼

       Feature Engineering

                 │

          ┌──────┴──────┐

          ▼             ▼

         BMI      Pulse Pressure

          └──────┬──────┘

                 ▼

        Feature Preprocessing

                 │

                 ▼

             SVM (RBF)

                 │

          ┌──────┴──────┐

          ▼             ▼

     Prediction     Probability

          │             │

          └──────┬──────┘

                 ▼

          Streamlit Result

```

---

# 🔮 Future Improvements

- 🔍 Hyperparameter optimization.

- 🔄 Cross-validation.

- 🧠 Explainable AI using SHAP.

- 📊 Prediction explanation.

- 📈 Model monitoring.

- ☁️ Cloud deployment.

- 🔐 Authentication and access control.

- 🏥 Integration with real clinical datasets.

- 📱 Mobile application.

- 🧪 Additional model validation.

---

# 👥 Team / Owners

This project was developed by:
-----------------------------

 ****Ammar Yasser****     

 ****Abdallah Essam****  

 ****Youssef Abdallah**** 

 ****Nada Mohamed****     

 ****Bassant Ibrahim****  

---

<h2>🎓 Academic Project</h2>

<p>NTI (Summer Training)</p>

<p>Machine Learning Program</p>

---

# ⚠️ Disclaimer

CardioInsight is an educational and research project.

The predictions generated by this application are not medical diagnoses and should not be used as a substitute for evaluation, diagnosis, or treatment by a qualified healthcare professional.

---

<p align="center">

  Made by the CardioInsight Team

</p>

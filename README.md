# 📱 Human Activity Recognition using LSTM

A Deep Learning based Human Activity Recognition (HAR) system that classifies human activities using smartphone accelerometer sensor data. The model is built using an LSTM (Long Short-Term Memory) network and provides real-time activity prediction through a Flask web application.

---

## 📌 Project Overview

Human Activity Recognition (HAR) is the task of identifying physical activities performed by a person using data collected from smartphone sensors.

This project uses an LSTM model to recognize activities from time-series accelerometer data.

---

## 🎯 Problem Statement

Classify physical activities (Walking, Jogging, Sitting, Standing, Upstairs, Downstairs) from smartphone sensor (accelerometer) time-series data using Deep Learning.

---

## 🛠 Technologies Used

- Python
- TensorFlow / Keras
- Flask
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Joblib
- HTML
- CSS

---

## 📂 Dataset

**Dataset Used:** MotionSense Dataset

Sensor Features:

- userAcceleration.x
- userAcceleration.y
- userAcceleration.z

Activities:

- Walking
- Jogging
- Sitting
- Standing
- Upstairs
- Downstairs

---

## 🧠 Model Architecture

- Input Layer
- LSTM Layer
- Dropout Layer
- Dense Layer
- Softmax Output Layer

Loss Function:

- Categorical Crossentropy

Optimizer:

- Adam

---

## 📊 Model Performance

Validation Accuracy:

**89.27%**

Evaluation Metrics:

- Accuracy
- Loss
- Classification Report
- Confusion Matrix

---

## 📁 Project Structure

```
Human-Activity-Recognition/

│── dataset/
│── static/
│   └── style.css
│
│── templates/
│   └── index.html
│
│── app.py
│── train.py
│── model.py
│── predict.py
│── har_model.keras
│── scaler.pkl
│── label_encoder.pkl
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Human-Activity-Recognition.git
```

Go to project directory

```bash
cd Human-Activity-Recognition
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open browser

```
http://127.0.0.1:5000
```

---

## 🚀 Features

- Human Activity Recognition using LSTM
- Time-Series Data Processing
- Data Normalization
- Sliding Window Technique
- Flask Web Application
- Real-Time Prediction Interface
- Responsive UI
- Model Save & Load
- Prediction Confidence

---

## 📈 Training Pipeline

1. Load MotionSense Dataset
2. Data Preprocessing
3. Feature Scaling
4. Sliding Window Creation
5. Train/Test Split
6. LSTM Model Training
7. Model Evaluation
8. Save Model

---

## 📊 Results

Activities Recognized:

- Walking
- Jogging
- Sitting
- Standing
- Upstairs
- Downstairs

Validation Accuracy:

**89.27%**

---

## 📷 Screenshots

Add screenshots here:

- Training Accuracy Graph
- Training Loss Graph
- Confusion Matrix
- Flask Dashboard

---

## 🔮 Future Improvements

- Android Application Integration
- Improved Real-Time Prediction
- Support for Gyroscope Data
- GRU and Transformer Models
- Cloud Deployment
- Better UI/UX

---

## 👨‍💻 Author

**Sorab Bhadautiya**

B.Tech CSE (AI & ML)

GLA University

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!

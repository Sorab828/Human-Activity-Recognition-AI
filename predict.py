import numpy as np
import joblib
from tensorflow.keras.models import load_model

model = load_model("har_model.keras")

scaler = joblib.load("scaler.pkl")
encoder = joblib.load("label_encoder.pkl")

sample = np.array([
    [0.12, -0.34, 0.91],
    [0.15, -0.31, 0.88],
    [0.18, -0.29, 0.90],
    [0.11, -0.35, 0.93],
    [0.14, -0.32, 0.89],
    [0.13, -0.30, 0.87],
    [0.17, -0.28, 0.91],
    [0.12, -0.33, 0.90],
    [0.15, -0.31, 0.88],
    [0.16, -0.29, 0.92],
] * 8)

sample = sample[:80]

sample = scaler.transform(sample)

sample = sample.reshape(1, 80, 3)

prediction = model.predict(sample, verbose=0)

predicted_class = np.argmax(prediction)

activity = encoder.inverse_transform([predicted_class])[0]

confidence = np.max(prediction) * 100

print("=" * 40)
print("Predicted Activity :", activity)
print("Confidence :", round(confidence, 2), "%")
print("=" * 40)
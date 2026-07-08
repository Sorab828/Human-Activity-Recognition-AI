from flask import Flask, render_template, jsonify
from tensorflow.keras.models import load_model
import joblib
import numpy as np
import requests
from collections import Counter

app = Flask(__name__)

# -----------------------------
# Load Model
# -----------------------------
model = load_model("har_model.keras")
scaler = joblib.load("scaler.pkl")
encoder = joblib.load("label_encoder.pkl")

# -----------------------------
# Phone IP
# -----------------------------
PHONE_IP = "192.168.29.182"
BASE_URL = f"http://{PHONE_IP}:8080"

WINDOW_SIZE = 80

sensor_buffer = []
prediction_history = []
previous_label = "Collecting..."

# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# Prediction API
# -----------------------------
@app.route("/predict")
def predict():

    global sensor_buffer
    global prediction_history
    global previous_label

    try:

        url = BASE_URL + "/get?accX&accY&accZ"

        response = requests.get(url, timeout=2)

        data = response.json()

        x = float(data["buffer"]["accX"]["buffer"][0])
        y = float(data["buffer"]["accY"]["buffer"][0])
        z = float(data["buffer"]["accZ"]["buffer"][0])

        sensor_buffer.append([x, y, z])

        # Wait until enough samples
        if len(sensor_buffer) < WINDOW_SIZE:

            return jsonify({
                "status": "collecting",
                "samples": len(sensor_buffer),
                "required": WINDOW_SIZE
            })

        # Keep latest WINDOW_SIZE samples
        sensor_buffer = sensor_buffer[-WINDOW_SIZE:]

        sample = np.array(sensor_buffer)

        sample = scaler.transform(sample)

        sample = sample.reshape(1, WINDOW_SIZE, 3)

        prediction = model.predict(sample, verbose=0)[0]

        confidence = float(np.max(prediction)) * 100

        current_label = encoder.inverse_transform(
            [np.argmax(prediction)]
        )[0]

        # -----------------------------
        # Confidence Threshold
        # -----------------------------
        if confidence >= 70:

            prediction_history.append(current_label)

            if len(prediction_history) > 5:
                prediction_history.pop(0)

            # Majority Voting
            final_label = Counter(
                prediction_history
            ).most_common(1)[0][0]

            previous_label = final_label

        else:

            final_label = previous_label

        return jsonify({

            "status": "success",

            "activity": final_label,

            "confidence": round(confidence, 2),

            "x": round(x, 3),

            "y": round(y, 3),

            "z": round(z, 3)

        })

    except Exception as e:

        return jsonify({

            "status": "error",

            "message": str(e)

        })


if __name__ == "__main__":
    app.run(debug=True)
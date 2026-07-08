
import os, glob
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from model import build_model

DATASET_PATH = "dataset/A_DeviceMotion_data/A_DeviceMotion_data"
WINDOW_SIZE = 80
STEP = 20
MAX_ROWS_PER_FILE = 500

activity_map = {
    "dws": "Downstairs",
    "jog": "Jogging",
    "sit": "Sitting",
    "std": "Standing",
    "ups": "Upstairs",
    "wlk": "Walking"
}

X_seq = []
y_seq = []

scaler = StandardScaler()
encoder = LabelEncoder()

# ---------- First pass : fit scaler ----------
all_samples = []

files = glob.glob(os.path.join(DATASET_PATH, "*", "*.csv"))

for file in files:
    folder = os.path.basename(os.path.dirname(file))
    key = folder.split("_")[0]

    if key not in activity_map:
        continue

    df = pd.read_csv(file).head(MAX_ROWS_PER_FILE)

    df = df[
        [
            "userAcceleration.x",
            "userAcceleration.y",
            "userAcceleration.z",
        ]
    ]

    all_samples.append(df)

all_samples = pd.concat(all_samples, ignore_index=True)
scaler.fit(all_samples)

# ---------- Label encoder ----------
encoder.fit(list(activity_map.values()))

# ---------- Create windows PER FILE ----------
for file in files:

    folder = os.path.basename(os.path.dirname(file))
    key = folder.split("_")[0]

    if key not in activity_map:
        continue

    label = encoder.transform([activity_map[key]])[0]

    df = pd.read_csv(file).head(MAX_ROWS_PER_FILE)

    X = df[
        [
            "userAcceleration.x",
            "userAcceleration.y",
            "userAcceleration.z",
        ]
    ].values

    X = scaler.transform(X)

    for i in range(0, len(X)-WINDOW_SIZE+1, STEP):
        X_seq.append(X[i:i+WINDOW_SIZE])
        y_seq.append(label)

X_seq = np.asarray(X_seq, dtype=np.float32)
y_seq = np.asarray(y_seq)

print("Sequences:", X_seq.shape)

X_train, X_test, y_train, y_test = train_test_split(
    X_seq,
    y_seq,
    test_size=0.2,
    random_state=42,
    stratify=y_seq
)

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

model = build_model(
    input_shape=(WINDOW_SIZE,3),
    num_classes=y_train.shape[1]
)

history = model.fit(
    X_train,
    y_train,
    validation_data=(X_test,y_test),
    epochs=20,
    batch_size=32
)

model.save("har_model.keras")
joblib.dump(scaler,"scaler.pkl")
joblib.dump(encoder,"label_encoder.pkl")

print("Model, scaler and encoder saved.")

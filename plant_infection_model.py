# plant_infection_model.py
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import os

# -----------------------------
# Load the trained model once
# -----------------------------
MODEL_PATH = r"D:\SIH\tomato_leaf_model_final.h5"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")

model = load_model(MODEL_PATH)

# -----------------------------
# Prediction function
# -----------------------------
def predict_leaf(pil_image):
    """
    Input: PIL.Image
    Output: (label, confidence)
    - label: "Healthy" or "Infected"
    - confidence: float 0-100
    """
    # Resize and preprocess
    img = pil_image.resize((224,224))
    img_array = np.array(img)/255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    pred = model.predict(img_array)[0][0]

    if pred > 0.5:
        label = "Infected"
        confidence = pred * 100
    else:
        label = "Healthy"
        confidence = (1 - pred) * 100

    return label, confidence

from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load model once
model = tf.keras.models.load_model("monkeypox_model.h5")

# Map model output index to class names (update according to your training labels)
index_to_class = {
    0: "chickenpox",
    1: "Eczema",
    2: "Lupus",
    3: "Measles",
    4: "Molluscum",
    5: "Monkeypox",
    6: "Normal",
    7: "Scabies"
}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/predict", methods=["POST"])
def predict():
    print("✅ PREDICT ROUTE HIT")  # DEBUG STEP

    if "image" not in request.files:
        print("❌ No image key in request")
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]

    if file.filename == "":
        print("❌ Empty filename")
        return jsonify({"error": "Empty filename"}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    try:
        # Preprocess image
        img = Image.open(filepath).convert("RGB").resize((224, 224))
        img = np.array(img) / 255.0
        img = np.expand_dims(img, axis=0)

        # Predict
        pred_probs = model.predict(img)
        pred_class_index = np.argmax(pred_probs)
        confidence = float(pred_probs[0][pred_class_index])
        result = index_to_class[pred_class_index]

        print(f"✅ Prediction success: {result} ({confidence*100:.2f}%)")

        return jsonify({
            "prediction": result,
            "confidence": round(confidence * 100, 2)
        })

    except Exception as e:
        print("🔥 ERROR:", str(e))
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)

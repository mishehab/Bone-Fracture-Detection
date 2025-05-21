from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from ultralytics import YOLO
import os

app = Flask(__name__)
CORS(app)

model = YOLO(r"C:\Users\User\OneDrive\Documents\4-1\IDP-2\bone fracture model\yolov8n-fracture.pt")
os.makedirs("uploads", exist_ok=True)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        file = request.files['image']
        file_path = os.path.join("uploads", file.filename)
        file.save(file_path)

        results = model.predict(file_path)
        predictions = results[0].boxes.cls.tolist()

        os.remove(file_path)  # optional
        return jsonify({"predictions": predictions})
    except Exception as e:
        print("❌ Error during prediction:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)

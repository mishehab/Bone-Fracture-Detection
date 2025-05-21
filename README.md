<h1 align="center">🦴 Bone Fracture Detection using YOLOv8</h1>

<p align="center">
  <img src="https://img.shields.io/badge/AI%20Model-YOLOv8-blue?style=flat-square" alt="Model Badge">
  <img src="https://img.shields.io/badge/Framework-Flask-orange?style=flat-square" alt="Framework">
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License">
</p>

<p align="center">
  A full-stack AI-powered web application to detect bone fractures from X-ray images using a YOLOv8 deep learning model.
</p>

<p align="center">
  <img src="https://via.placeholder.com/400x300?text=Upload+X-ray+Image" width="400" alt="Preview Image">
</p>

---

## 🚀 Features

<ul>
  <li>🧠 YOLOv8 model trained on 10 fracture classes</li>
  <li>📸 Upload and preview X-ray images</li>
  <li>🔍 Predict fractures and display the class(es)</li>
  <li>📄 Downloadable text report after prediction</li>
  <li>🌈 Beautiful modern UI with animated feedback</li>
</ul>

---

## 📁 Project Structure

bone-fracture-detection/
├── app.py # Flask backend API
├── human_bone_fractures_image.ipynb # Notebook for train the model
├── yolov8n-fracture.pt # Trained YOLOv8 model
├── templates/
│ └── index.html # Frontend HTML interface
├── static/ # (Optional) folder for CSS/JS
├── uploads/ # Temporary storage for uploaded images
└── README.md # Project description


---

## 🧪 How to Run Locally

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/yourusername/bone-fracture-detection.git
   cd bone-fracture-detection

2. **Install Python Dependencies**

   ```bash
   pip install flask flask-cors ultralytics

3. **Start the Flask Server**

   ```bash
   python app.py

4. **Open your browser and visit**

http://127.0.0.1:5000/

5. **Upload an X-ray Image**

<ul>
  <li>The app will show a preview</li>
  <li>Click Detect Fracture</li>
  <li>View the result and download the report</li>
</ul>

🧠 Model Classes Detected
Class ID	Fracture Type
0	Comminuted
1	Greenstick
2	Healthy
3	Linear
4	Oblique Displaced
5	Oblique
6	Segmental
7	Spiral
8	Transverse Displaced
9	Transverse

🌟 Future Ideas
✅ Add doctor recommendation output

✅ Support image annotations or bounding boxes

✅ Add drag-and-drop image upload

✅ Deploy to Render or Hugging Face Spaces

✅ Patient record history & login system

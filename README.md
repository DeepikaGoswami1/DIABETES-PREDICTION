# DiaPredict AI - Diabetes Prediction Web App

A modern, machine-learning-powered web application that predicts a user's risk of diabetes based on medical metrics. Built with a sleek 3D-styled user interface, this project evaluates 8 clinical parameters in real-time to provide an instant, highly accurate risk assessment.

## 🚀 Features
- **Machine Learning Integration**: Utilizes a pre-trained Support Vector Machine (SVM) / Random Forest model for accurate classification.
- **Modern UI/UX**: A beautiful, fully responsive interface featuring glassmorphism, CSS gradients, micro-animations, and dynamic 3D-hover effects.
- **Fast & Secure**: No user data is saved or stored; calculations and predictions happen instantly.
- **Cloud-Ready**: Prepared with `gunicorn` and a `Procfile` for one-click deployment on platforms like Render, Heroku, or AWS.

## 🛠️ Tech Stack
- **Frontend**: HTML5, Vanilla CSS3 (Custom Design System), Jinja2 Templating
- **Backend**: Python 3.x, Flask, Gunicorn
- **Machine Learning**: Scikit-Learn, Pandas, NumPy
- **Deployment**: Configured for Render / Heroku

## ⚙️ How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/diabetes-prediction-pro.git
   cd diabetes-prediction-pro
   ```

2. **Create a Virtual Environment (Optional but recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask Application:**
   ```bash
   python app.py
   ```
   *The application will now be running on `http://127.0.0.1:5000/`*

## 🌐 Deployment (Render)
This project is configured right out of the box for Render.
1. Connect this GitHub repository to Render as a **Web Service**.
2. Build Command: `pip install -r requirements.txt`
3. Start Command: `gunicorn app:app` (or Render will automatically detect it via the included `Procfile`).
Public link

## 📊 Dataset Used
The model was trained on medical data featuring 8 specific diagnostic measurements (Pregnancies, Glucose, Blood Pressure, Skin Thickness, Insulin, BMI, Diabetes Pedigree Function, and Age).

---
*Disclaimer: This tool is strictly for educational and informational purposes and does not replace professional medical advice.*

from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        features = [float(x) for x in request.form.values()]
        prediction = model.predict([features])

        if prediction[0] == 1:
            result = "High Risk of Diabetes (Consult a Doctor)"
        else:
            result = "Low Risk of Diabetes"

        return render_template("predict.html", prediction_text=result, result_class="text-risk" if prediction[0]==1 else "text-safe")
    
    return render_template("predict.html")

if __name__ == "__main__":
    app.run(debug=True)
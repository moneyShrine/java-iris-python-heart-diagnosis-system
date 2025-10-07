from flask import Flask, request, jsonify
import joblib as jb
import numpy as np

app = Flask(__name__)

model = jb.load("random_forest_hrt_diag")

@app.route("/")
def home():
    return "Heart Diagnosis Model API is running ✅"


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = np.array(data["features"]).reshape(1, -1)
    prediction = model.predict(features)[0]
    return jsonify({"prediction": str(prediction)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
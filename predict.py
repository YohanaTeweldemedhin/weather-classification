from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load your model once when the server starts
model = joblib.load("weather_model.pkl")
print("Model loaded successfully!")

# Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get JSON data from POST request
    
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    # Convert input to DataFrame
    if isinstance(data, dict):
        features = pd.DataFrame([data])
    elif isinstance(data, list):
        features = pd.DataFrame(data)
    else:
        return jsonify({"error": "Invalid input format"}), 400

    # Make prediction
    try:
        predictions = model.predict(features)
        return jsonify({"predictions": predictions.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Test route
@app.route('/')
def home():
    return "Weather Prediction API is running!"

if __name__ == "__main__":
    app.run(debug=True)

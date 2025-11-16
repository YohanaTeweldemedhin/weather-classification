import joblib
import pandas as pd


def load_model(file_name):   
   model= joblib.load(file_name)
   print("Model loaded successfully!")
   return model


def predict_weather(model,features):

    if isinstance(features, dict):
        features = pd.DataFrame([features])
    elif isinstance(features, list):
        features = pd.DataFrame(features)    
    predictions = model.predict(features)    
    return predictions


features = {
    "Temperature": 3,
    "Humidity": 83,
    "Wind Speed": 6,
    "Precipitation (%)": 66,
    "Cloud Cover":"overcast",
    "Atmospheric Pressure": 999.44,
    "UV Index": 0,
    "Visibility (km)": 1,
    "Season": "Winter",
    "Location": "mountain"
}
model = load_model("weather_model.pkl")
pred = predict_weather(model,features)
print("Predicted Weather Type:", pred[0])




   




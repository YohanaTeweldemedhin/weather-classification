# Weather Prediction Application


This project is a machine learning–powered Weather Prediction API built using Flask. It loads a trained model (weather_model.pkl) and provides predictions through a REST API endpoint. Users can send weather-related input , and the API responds with predicted weather conditions. This application demonstrates model deployment, API development, and real-time prediction handling. The application accepts the following features as input

1. Temperature
2. Humidity
3. Wind Speed
4. Precipitation (%)
5. Cloud Cover
6. Atmospheric Pressure
7. UV Index
8. Visibility (km)
9. Season
10. Location

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Deployment](#deployment)
- [Usage](#usage)


## Overview

This project provides a REST API to predict weather conditions based on input features. The API uses a pre-trained machine learning model (`weather_model.pkl`) and returns predictions in JSON format.

Built with:
- pandas==2.3.2
- numpy==2.3.3
- Flask==3.1.2
- matplotlib==3.10.6
- seaborn==0.13.2
- scikit-learn==1.7.2
- joblib==1.5.2

## Features

- Predict weather using a machine learning model
- Accepts JSON input with one or multiple records
- Returns predictions as a JSON response
- Easy to deploy locally or on a server

### Install Dependencies
#### --> Install all required packages using:

```bash
pip install -r requirements.txt

```


### Add the Trained Model
Place the trained model file **weather_model.pkl** in the project root directory (same folder as `app.py`).

### Run the Flask Application

Start the server with:

```bash
python app.py

http://127.0.0.1:5000/


```


### Test the API

- Root endpoint: `GET /`

Should return: "Weather Prediction API is running!"

- Prediction endpoint: `POST /predict`
Send JSON data, for example:
```json
{
  "temperature": 25,
  "humidity": 23,
  "wind_speed": 12,
  "precipitation":6,
  "Cloud cover":"Overcast",
  "Atmospheric pressure":999.44,
  "UV index":0,
  "Visibility":1,
  "Season":"Winter",
  "Location":"Mountain"
}

{
  "predictions": ["Cloudy"]
}

```


![Screenshot](images/postman_model_output.)
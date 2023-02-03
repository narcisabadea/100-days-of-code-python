# Bearer authentication (also known as token authentication) is an HTTP authentication scheme that involves security tokens.
# The name “Bearer authentication” basically means “give access to the bearer of this token.”
# The security token or “bearer token” is just a cryptic string.

import requests
from datetime import datetime
from configparser import ConfigParser


def _get_api_key():
    config = ConfigParser(interpolation=None)
    config.read("../secrets.ini")
    keys = {
        "google_sheet":  config["google_sheet"],
        "nutritionix": config["nutritionix"],
    }
    return keys


keys = _get_api_key()

APP_ID = keys["nutritionix"]["APP_ID"]
API_KEY = keys["nutritionix"]["API_KEY"]
GOOGLE_SHEET_KEY = keys["google_sheet"]["Authorization"]

# Get exercises
exercise_text = input("Tell me which exercises you did: ")
google_sheet_endpoint = "https://api.sheety.co/d27e937eed74c1cbabaf96fd1251c54c/pythonDay38MyWorkouts/workouts"

post_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
post_exercise_params = {
    "query": exercise_text,
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
    "Content-Type": "application/json",
}

google_sheet_headers = {
    "Authorization": GOOGLE_SHEET_KEY
}

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")

# Get the calories of those exercises
response = requests.post(url=post_exercise_endpoint,
                         json=post_exercise_params, headers=headers)

result = response.json()

exercises = result["exercises"]

# Post them in google sheet by using https://sheety.co/
# https: // docs.google.com/spreadsheets/d/1MwrWkPpjrtmW6uXKX66hNhQDLXycVdT30y4JJzEcEq8/edit#gid=0

for exercise in exercises:
    request_body = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["user_input"].title(),
            "duration": round(exercise["duration_min"]),
            "calories": round(exercise["nf_calories"])
        }
    }
    response = requests.post(url=google_sheet_endpoint,
                             json=request_body, headers=google_sheet_headers)
    print(response)

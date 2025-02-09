import requests
from datetime import datetime
from config import *

user_exercise = input("Tell me which exercise you did: ")

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

exercise_params = {
    "query": user_exercise,
    "weight_kg": 59,
    "height_cm": 167,
    "age": 20
}

exercise_endpoint = EXERCISE_ENDPOINT

exercise = requests.post(exercise_endpoint, json=exercise_params, headers=headers)
exercise_result = exercise.json()


today = datetime.now()

sheety_endpoint = SHEET_ENDPOINT

for exercise in exercise_result["exercises"]:
    calories = exercise_result["exercises"][0]["nf_calories"]
    name = exercise_result["exercises"][0]["name"]
    duration = exercise_result["exercises"][0]["duration_min"]

    sheety_body = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%X"),
            "exercise": name.title(),
            "duration": duration,
            "calories": calories,
        }
    }

sheety = requests.post(sheety_endpoint, json=sheety_body, auth=(USERNAME, TOKEN))
sheety_result = sheety.json()
print(sheety.status_code)
print(sheety_result)

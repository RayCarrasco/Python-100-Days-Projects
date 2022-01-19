import os
import requests
import datetime

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
SITE = "https://trackapi.nutritionix.com"
END_POINT = f"{SITE}/v2/natural/exercise"

SHEETY_API_GET = os.environ.get("SHEETY_API_GET")
SHEETY_API_POST = os.environ.get("SHEETY_API_POST")

USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")


def nutritionix_api_communication(message):
    headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
    }

    parameters = {
        "query": f'{message}',
        "gender": "male",
        "weight_kg": 56,
        "height_cm": 172,
        "age": 27,
    }

    response = requests.post(url=END_POINT, headers=headers, json=parameters)
    for activity in response.json()["exercises"]:
        sheety_api_post(activity["name"].title(), int(activity["duration_min"]), activity["nf_calories"])


def sheety_api_post(exercise, duration, calories):
    dt = datetime.datetime.now()
    date = dt.strftime("%Y/%m/%d")
    time = dt.strftime("%X")

    parameters = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories,
        }
    }

    response = requests.post(url=SHEETY_API_POST, json=parameters, auth=(USER, PASSWORD))
    response.raise_for_status()


def main():
    nutritionix_api_communication(input("Tell me which exercises you did: "))


if __name__ == '__main__':
    main()

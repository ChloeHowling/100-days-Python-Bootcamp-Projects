import requests
from datetime import datetime
import os


SHEETY_TOKEN = "asserdtfytt53465423wesd"
NUTR_APP_ID = "9e22f9b2"
NUTR_API_KEY = "762ec93bc2b30064270b64426515b4c6"

# os.environ["NUTR_APP_ID"] = NUTR_APP_ID
# os.environ["NUTR_API_KEY"] = NUTR_API_KEY
# NUTR_APP_ID = os.environ.get('NUTR_APP_ID')
# NUTR_API_KEY = os.environ.get('NUTR_API_KEY')
#
# NUTR_APP_ID = os.environ.get("NUTR_APP_ID")
# NUTR_API_KEY = os.environ.get("NUTR_API_KEY")


def get_nutrition_data(query):
    endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
    headers = {
        "x-app-id": NUTR_APP_ID,
        "x-app-key": NUTR_API_KEY,
    }
    params = {
        "query": query,
        "gender": "female",
        "weight_kg": 57.6,
        "height_cm": 162,
        "age": 24
    }

    response = requests.post(url=endpoint, json=params, headers=headers)
    print(response.json())
    return response.json()["exercises"]


def update_sheet(nutrition_data):
    sheety_endpoint = "https://api.sheety.co/3c75b974a9671147f405a3644dcf0a08/myWorkouts/workouts"
    # Write a new row
    # Current Date | Time | Exercise | Duration | Calorie

    today = datetime.now()
    date = today.strftime('%d/%m/%Y')
    time = today.strftime('%H:%M:%S')
    exercise = nutrition_data[0]["name"]
    duration = nutrition_data[0]["duration_min"]
    calorie = nutrition_data[0]["nf_calories"]

    sheety_row = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise,
            "duration": duration,
            "calories": calorie
        }
    }

    sheety_headers = {
        "Authorization": f"Bearer {SHEETY_TOKEN}"
    }

    response = requests.post(url=sheety_endpoint, json=sheety_row, headers=sheety_headers)
    print(response.text)
    print(response)


while True:
    user_input = input("What did you do for exercise today?\n")
    data = get_nutrition_data(user_input)
    print(data)
    y_n = input("\nIs the above information correct? (y/n) ").lower()

    if y_n == 'y':
        update_sheet(data)
    elif y_n == 'q':
        break

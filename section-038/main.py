from dotenv   import load_dotenv
from datetime import datetime 
import requests
import os

load_dotenv()
NUTRITIONIX_API_KEY = os.getenv("NUTRITIONIX_API_KEY")
NUTRITIONIX_APP_ID  = os.getenv("NUTRITIONIX_APP_ID")
USERNAME            = os.getenv("USERNAME")
USERNAME_AUTH            = os.getenv("USERNAME_AUTH")
PASSWORD            = os.getenv("PASSWORD")
BEARER_TOKEN            = os.getenv("BEARER_TOKEN")

PROJECT_NAME = "my workouts"
SHEET_NAME = "my-workouts"

# User data
GENDER = "male",
WEIGHT_KG = 60.5,
HEIGHT_CM = 167.0,
AGE = 22

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = f"https://api.sheety.co/{USERNAME}/my-workouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

# parameters =  {
#     "query":exercise_text,
#     "gender":GENDER,
#     "weight_kg":WEIGHT_KG,
#     "height_cm":HEIGHT_CM,
#     "age":AGE
# }

parameters = {
 "query":exercise_text,
 "gender":"female",
 "weight_kg":72.5,
 "height_cm":167.64,
 "age":30
}

headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY
}

response = requests.post(EXERCISE_ENDPOINT, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_data = {
        SHEET_NAME: {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    #Basic Authentication
    sheet_response = requests.post(
        SHEETY_ENDPOINT, 
        json=sheet_data, 
        auth=(
            USERNAME_AUTH, 
            PASSWORD,
        )
    )
    
print(sheet_response.status_code)

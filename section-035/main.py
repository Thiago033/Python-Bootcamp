import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
API_KEY = os.getenv("API_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
MY_NUMBER = os.getenv("MY_NUMBER")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

MY_LAT = 50
MY_LNG = -50

parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": API_KEY,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_id = weather_data["weather"][0]["id"]

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

if int(weather_id) < 700:
    print("True")
    message = client.messages \
                    .create(
                        body="It's going to rain today!",
                        from_=TWILIO_PHONE_NUMBER,
                        to=MY_NUMBER
                    )

    print(message.status)
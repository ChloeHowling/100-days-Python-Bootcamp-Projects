import requests
from twilio.rest import Client

PHONE = "+19514325275"
account_sid = "AC4db021befdfdeb7a7d313888254eaefe"
auth_token = "e5878590c03c07a478f1331a71846819"

OWM_END = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "9d4bcb2365a27f5ce070ac4e85e4ff97"
MY_LAT = 34.052235
MY_LONG = -118.243683

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_END, params=parameters)
response.raise_for_status()

weather_data = response.json()["hourly"][:12]
will_rain = False


for hour in weather_data:
    weather_id = int(hour["weather"][0]["id"])
    if weather_id < 700:
        will_rain = True
        break

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today! Remember to bring an ☔",
            from_=PHONE,
            to='+18015778961'
    )

    print(message.status)
else:
    print("No rain.")




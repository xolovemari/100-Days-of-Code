import requests
from twilio.rest import Client

account_sid = "example"
auth_token = "example"

# random place thats raining
weather_params = {
    "lat": -3.106390,
    "lon": -60.026291,
    "appid": "example",
    "cnt": 4,
}

response = requests.get(url="http://api.openweathermap.org/data/2.5/forecast", params=weather_params)
response.raise_for_status()
weather_data = response.json()

weather_ids = [item["weather"][0]["id"] for item in weather_data["list"][:4]]

if any(id < 700 for id in weather_ids):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
  body="It's going to rain today. Remember to bring an umbrella.",
  from_='+0000000000',
  to='+00000000000'
)

print(message.status)
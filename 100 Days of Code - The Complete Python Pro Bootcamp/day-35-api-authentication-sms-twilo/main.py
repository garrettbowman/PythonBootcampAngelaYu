import os
import requests
from twilio.rest import Client
# Adjusted for python anywhere
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint= "https://api.openweathermap.org/data/2.5/forecast?"
api_key = "x"
MY_LAT = 42.521439
MY_LNG = -83.020180
my_sid = "x"
my_auth = "x"

params = {
    "appid":api_key,
    "lat":18.290934,
    "lon":-77.543962,
    "cnt":4,
}

response = requests.get(OWM_Endpoint, params=params)
response.raise_for_status()

weather_data = response.json()
will_rain = False
for x in range(0,4):
    code = int(weather_data["list"][x]["weather"][0]["id"])
    if code <= 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(my_sid,my_auth,http_client=proxy_client)
    message = client.messages.create(
        body="It will rain today, bring an umbrella!",
        from_="whatsapp:+x",
        to="whatsapp:+x",
    )

    print(message.status)

import requests

OWM_Endpoint= "https://api.openweathermap.org/data/2.5/forecast?"
api_key = "0cb0cd717da2d0755003c7b2775f77dd"
MY_LAT = 42.521439
MY_LNG = -83.020180

params = {
    "appid":api_key,
    "lat":18.290934,
    "lon":-77.543962,
    "cnt":4,
}

response = requests.get(OWM_Endpoint, params=params)
response.raise_for_status()

weather_data = response.json()

for x in range(0,4):
    code = int(weather_data["list"][x]["weather"][0]["id"])
    if code <= 700:
        print("bring an umbrella")
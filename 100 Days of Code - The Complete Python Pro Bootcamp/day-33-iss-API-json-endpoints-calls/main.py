import requests
import datetime as dt
MY_LAT = 42.521439
MY_LONG = -83.020180


# iss_response = requests.get("http://api.open-notify.org/iss-now.json")
# iss_response.raise_for_status()
#
# data = iss_response.json()
#
# print(data)
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss = (longitude,latitude)
# print(iss)
parameters = {
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0
}


response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
sun_data = response.json()
print(sun_data)

sunrise = sun_data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = sun_data["results"]["sunset"].split("T")[1].split(":")[0]

# s_split = sunrise.split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
# print(s_split)


now = dt.datetime.now()
print(now.hour)
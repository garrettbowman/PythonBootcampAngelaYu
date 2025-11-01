import requests
from datetime import datetime
import os

# os.environ["nutritionix_endpoint"] =  "https://trackapi.nutritionix.com/v2/natural/exercise"
os.environ["nutritionix_endpoint"] =  "https://trackapi.nutritionix.com/v2/natural/exercise"
#
APP_ID = os.environ.get("nutritionix_endpoint")
print(APP_ID)
# headers = {
#     "x-app-id": APP_ID,
#     "x-app-key": API_KEY,
#     # "Content-Type": "application/json"
# }
# # user_input = input("Tell me what exercise you did: ")
# nut_params = {
#     "query": "10 hours of walking"
# }
#
# response = requests.post(url=nutritionix_endpoint,json=nut_params,headers=headers)
# response.raise_for_status()
#
# result = response.json()
# print(result)
# print(response.text)

SHEETY_API = "x"

headers = {
}

params= {
    "Date":str(datetime.now()),
    "Time":"233",
    "Exercise":"walking",
    "Duration":"2 hours",
    "Calories":"2313"
}

response2 = requests.post(url=SHEETY_API,json=params, headers=headers)
response2.raise_for_status()

print(response2)
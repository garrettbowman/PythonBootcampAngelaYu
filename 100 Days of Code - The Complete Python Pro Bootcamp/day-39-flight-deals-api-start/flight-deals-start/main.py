#This file will need to u
# se the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from http.client import responses

from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
import requests
import pandas

SHEETY_API_ENDPOINT = "x"
AMADEUS_ENDPOINT = "x"
AMADEUS_API_KEY = "x"
AMADEUS_API_SECRET = "x"
AMADEUS_TOKEN = "x"
FLIGHT_SEARCH_ENDPOINT = 'https://test.api.amadeus.com/v1/shopping/flight-destinations'
BASE_URL= "https://test.api.amadeus.com/v1"
BASE_URL2= "https://test.api.amadeus.com/v2"
LOC_ENDPOINT ="/reference-data/locations"
DESTINATION_SEARCH_ENDPOINT=f"{BASE_URL}{LOC_ENDPOINT}"

# {'type': 'amadeusOAuth2Token', 'username': 'x@gmail.com', 'application_name': 'flightSearch', 'client_id': 'x', 'token_type': 'Bearer', 'access_token': 'x', 'expires_in': 1799, 'state': 'approved', 'scope': ''}

# response = requests.get(SHEETY_API_ENDPOINT)

# print(response.json())

token_header = {
    "content-type": "application/x-www-form-urlencoded"
}
token_param = {
    "grant_type" :"client_credentials",
    "client_id":AMADEUS_API_KEY,
    "client_secret":AMADEUS_API_SECRET
}

response2 = requests.post("https://test.api.amadeus.com/v1/security/oauth2/token",
                          headers=token_header,data=token_param)

token = response2.json()["access_token"]
print(token)
AMADEUS_HEADER = {
    "Authorization": f"Bearer {token}",
    # "Content-Type":"application/json"
    # "accept": "application/vnd.amadeus+json"
}
data_manager = DataManager(token, AMADEUS_HEADER)
data_manager.get_sheet()
flight_search = FlightSearch(token,AMADEUS_HEADER,data_manager.data)
flight_data = FlightData(token,AMADEUS_HEADER,data_manager.data)

# for x in range(0,1):
for x in range(0,len(data_manager.data["prices"])):
    code = data_manager.data["prices"][x]["iataCode"]
    price = data_manager.data["prices"][x]["lowestPrice"]
    print(code,price)
    flight_search.lookup_flights(code,price)

flight_data.process_data(flight_search.remember)

if flight_data.origins:
    notify = NotificationManager(flight_data.origins, flight_data.dates,flight_data.destination, flight_data.prices)
    notify.create_messages()
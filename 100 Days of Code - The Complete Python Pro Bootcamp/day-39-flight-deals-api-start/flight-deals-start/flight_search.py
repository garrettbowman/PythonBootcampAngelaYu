from datetime import datetime, timedelta

import requests
import pandas
import json

BASE_URL= "https://test.api.amadeus.com/v1"
BASE_URL2= "https://test.api.amadeus.com/v2"
LOC_ENDPOINT ="/reference-data/locations/cities"
FLIGHT_ENDPOINT = "/shopping/flight-offers"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, token, ah: dict,data):
        self.token = token
        self.AMADEUS_HEADER = ah
        self.data=data
        self.remember = []

    def lookup_flights(self,code,price):
        starting_date = datetime(2025, 12, 1)
        date = starting_date
        days=10
        for x in range(days):
            flight_params={
                "originLocationCode":"DTW",
                "destinationLocationCode":code,
                "departureDate":date.strftime("%Y-%m-%d"),
                "adults":1,
                "currencyCode":"USD",
                "maxPrice":price

            }
            response = requests.get(f"{BASE_URL2}{FLIGHT_ENDPOINT}",headers=self.AMADEUS_HEADER,params=flight_params)
            print(response.json())
            results = response.json()
            if results["meta"]["count"] != 0:
                self.remember.append(results)
            date += timedelta(days=1)
        print(self.remember)

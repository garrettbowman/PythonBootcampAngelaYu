import requests
import pandas
import json

BASE_URL= "https://test.api.amadeus.com/v1"
BASE_URL2= "https://test.api.amadeus.com/v2"
LOC_ENDPOINT ="/reference-data/locations/cities"


class FlightData:

    #This class is responsible for structuring the flight data.
    def __init__(self, token, ah: dict,data):
        self.token = token
        self.AMADEUS_HEADER = ah
        self.data = data
        self.jsons = []
        self.dates = []
        self.origins = []
        self.destination = []
        self.prices = []

    def process_data(self,jsons):
        self.jsons = jsons

        for x in range(0,len(jsons)):
            self.origins.append(self.jsons[x]["data"][0]["itineraries"][0]
                                ["segments"][0]['departure']["iataCode"])
            self.dates.append(self.jsons[x]["data"][0]["itineraries"][0]
                                ["segments"][0]['departure']["at"].split("T")[0])
            self.destination.append(self.jsons[x]["data"][0]["itineraries"][0]
                                ["segments"][-1]["arrival"]["iataCode"])
            self.prices.append(self.jsons[x]["data"][0]["price"]["total"])

        print(self.origins)
        print(self.dates)
        print(self.destination)
        print(self.prices)

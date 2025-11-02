SHEETY_API_ENDPOINT = "x"
import requests
import pandas
import json

BASE_URL= "https://test.api.amadeus.com/v1"
BASE_URL2= "https://test.api.amadeus.com/v2"
LOC_ENDPOINT ="/reference-data/locations/cities"
DESTINATION_SEARCH_ENDPOINT=f"{BASE_URL}{LOC_ENDPOINT}"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self,token, ah : dict):
        self.token = token
        self.AMADEUS_HEADER = ah
        self.data = {}
        self.df = {}
        self.cities = []
        self.codes = []


    def get_sheet(self):
        # response = requests.get(SHEETY_API_ENDPOINT)
        response = {'prices': [{'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 780, 'id': 4}, {'city': 'Hong Kong', 'iataCode': 'HKG', 'lowestPrice': 711, 'id': 5}, {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7}, {'city': 'Dublin', 'iataCode': 'DBN', 'lowestPrice': 378, 'id': 10}]}
        # response = {'prices': [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 100, 'id': 2}, {'city': 'Frankfurt', 'iataCode': 'FRA', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 780, 'id': 4}, {'city': 'Hong Kong', 'iataCode': 'HKG', 'lowestPrice': 711, 'id': 5}, {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7}, {'city': 'Dublin', 'iataCode': 'DBN', 'lowestPrice': 378, 'id': 10}]}


        # self.data = response.json()
        self.data = response

        self.df = pandas.DataFrame(self.data).to_dict()

        print(self.data)

        for x in range(0,len(self.df["prices"])):
            self.cities.append(self.df["prices"][x]["city"])

        # self.cities = self.df["prices"]["city"]
        print(self.cities)
        self.get_codes()
        for x in range(0,len(self.df["prices"])):
            self.df["prices"][x]["iataCode"] = self.codes[x]

        print(self.df)
        # upload = pandas.DataFrame.from_dict(self.data["prices"]).reset_index(drop=True)
        # records = json.loads(upload.to_json(orient="records"))
        #
        #
        # real_up = {"prices": records}
        upload = pandas.DataFrame.from_dict(self.data["prices"]).reset_index(drop=True)

        # Instead of json.loads(upload.to_json(...))
        records = upload.to_dict(orient="records")

        self.data = {"prices": records}

        print(self.data)

        # for x in range(0,len(self.data["prices"])):
        #
        #     update_params={"price":self.data["prices"][x]}
        #
        #     print(update_params)
        #     response = requests.put(f"https://api.sheety.co/2323ad58d753cd56b0defc99a297d01a/flightDeals/prices/{x+2}",json=update_params)
        #     response.raise_for_status()




    def get_codes(self):
        index = 0
        for city in self.cities:
            dest_search_params = {
                # "subType":"CITY",
                'keyword':f"{city}"
            }

            response3 = requests.get(DESTINATION_SEARCH_ENDPOINT,headers=self.AMADEUS_HEADER,params=dest_search_params)

            # print(response3.json()["data"])
            self.codes.append(response3.json()["data"][0]["iataCode"])
        print(self.codes)
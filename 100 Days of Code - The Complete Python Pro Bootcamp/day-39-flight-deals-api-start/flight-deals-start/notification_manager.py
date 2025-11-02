import requests

# from twilio.rest import Client

TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"
VIRTUAL_TWILIO_NUMBER = "your virtual twilio number"
VERIFIED_NUMBER = "your own phone number verified with Twilio"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self,origins,dates, destination, prices):
        self.origins = origins
        self.dates = dates
        self.destination = destination
        self.prices = prices
        self.messages = []

    def create_messages(self):
        for x in range(0,len(self.origins)):
            message = (f"A flight from {self.origins[x]} to {self.destination[x]}"
                       f" on {self.dates[x]} only {self.prices[x]}!")
            self.messages.append(message)

        print(self.messages)

    def send_messages(self):
        pass
        # client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

        #  Send each  as a separate message via Twilio.
        # for mes in messages:
        #     message = client.messages.create(
        #         body=mes,
        #         from_=VIRTUAL_TWILIO_NUMBER,
        #         to=VERIFIED_NUMBER
        #     )

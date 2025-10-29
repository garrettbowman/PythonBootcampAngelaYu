from twilio.rest import Client
import requests
import os
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"


account_sid = "__YOUR_TWILIO_ACCOUNT_ID__"
auth_token = "__YOUR_TWILIO_AUTH_TOKEN__"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

print(os.getenv("ALPHAVANTAGE_API_KEY"))

stock_params = {
    "apikey" : os.getenv("ALPHAVANTAGE_API_KEY"),
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,

}

response = requests.get(STOCK_ENDPOINT,stock_params)
# print(response.json())
yesterday = response.json()["Time Series (Daily)"]["2025-10-28"]["4. close"]
b_yesterday = response.json()["Time Series (Daily)"]["2025-10-27"]["4. close"]

pd = abs(float(yesterday)-float(b_yesterday))/float(b_yesterday)
reg_pd = (float(yesterday)-float(b_yesterday))/float(b_yesterday)
print(pd)
if pd >0.05:
    print("get news")


    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

news_params = {
    "apiKey" : os.getenv("NEWS_API_KEY"),
    "q":COMPANY_NAME,
    "searchIn":"title",
}
response2 = requests.get(NEWS_ENDPOINT,news_params)
articles = response2.json()["articles"][:3]
# print(articles)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
reformat = [(item["title"],item["description"]) for item in articles]
print(reformat)
#TODO 9. - Send each article as a separate message via Twilio.

for article in range(0,len(reformat)):
    if reg_pd < 0:
        symbol = "🔻"
    else:
        symbol = "🔺"

    message = f"""
    {STOCK_NAME}: 🔺  {round(pd*100)}%
    Headline: {reformat[article][0]} 
    Brief: {reformat[article][1]}
    """
    print(message)


    # client = Client(account_sid, auth_token)
    # message = client.messages \
    #     .create(
    #     body=f"{message}",
    #     from_="YOUR TWILIO VIRTUAL NUMBER",
    #     to="YOUR TWILIO VERIFIED REAL NUMBER"
    # )
    # print(message.status)


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


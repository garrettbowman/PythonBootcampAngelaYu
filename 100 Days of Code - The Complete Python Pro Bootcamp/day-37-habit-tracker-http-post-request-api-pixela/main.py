from calendar import month

import requests
from datetime import datetime

USERNAME = "garrettbow"
TOKEN = "wr34t34wer4w4tttfdx"

pixela_endpoint = "https://pixe.la/v1/users"

user_params= {
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor":"yes",

}

# response =requests.post(url = pixela_endpoint, json=user_params)
#
# print(response.text)

graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"

graph_params = {

    "id":"graph1",
    "name":"my cycling graph",
    "unit":"km",
    "type":"float",
    "color": "kuro",
}

headers = {
    "X-USER-TOKEN" : TOKEN
}
graph_response = requests.post(graph_endpoint,json=graph_params,headers=headers)
# today=datetime.now()
today=datetime(month=9,day=23,year=2025 )

post_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1"
post_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "2",

}
graph_post = requests.post(url=post_endpoint,json=post_params,headers=headers)

put_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1/{today.strftime("%Y%m%d")}"

put_params = {
    "quantity":"792"

}
graph_put = requests.put(url=put_endpoint,json=put_params,headers=headers)



pixel_del = requests.delete(url=put_endpoint,headers=headers)
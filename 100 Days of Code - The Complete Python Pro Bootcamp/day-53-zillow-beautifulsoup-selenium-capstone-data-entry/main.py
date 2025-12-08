from bs4 import BeautifulSoup
import requests


header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
zillow_url = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(url=zillow_url, headers=header)

soup = BeautifulSoup(response.text, 'html.parser')


from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# Import exceptions
from selenium.common.exceptions import TimeoutException, NoSuchElementException

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
zillow_url = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(url=zillow_url, headers=header)

soup = BeautifulSoup(response.text, 'html.parser')

houses = soup.select()
print(houses)

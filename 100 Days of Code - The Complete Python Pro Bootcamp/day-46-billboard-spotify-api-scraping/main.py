import requests
from bs4 import BeautifulSoup


billboard_base = "https://www.billboard.com/charts/hot-100/"
header = {"USER-AGENT":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}


day = input("What day would you like to travel to? YYYY-MM-DD")


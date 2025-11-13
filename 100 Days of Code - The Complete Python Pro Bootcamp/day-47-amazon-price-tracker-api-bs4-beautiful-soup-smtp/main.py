import os
from bs4 import BeautifulSoup
import smtplib
import requests
from dotenv import load_dotenv


BUY_PRICE = 100
load_dotenv()
headers= {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Chromium\";v=\"142\", \"Google Chrome\";v=\"142\", \"Not_A Brand\";v=\"99\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
  }
my_email = os.getenv("EMAIL_ADDRESS")
my_password = os.getenv("EMAIL_PASSWORD")

# response = requests.get("https://appbrewery.github.io/instant_pot/",headers=headers)
# response = requests.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1",headers=headers)
response = requests.get("https://www.amazon.com/gp/product/B00N9N6GOY/ref=sw_img_1?smid=ATVPDKIKX0DER&th=1",headers=headers)
ip = response.text
soup = BeautifulSoup(ip, "html.parser")
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36","Accept-Language":"en-US,en;q=0.9"}


price = float(soup.find(name="span", class_="aok-offscreen").getText().split("$")[1].split(" ")[0])
print(price)

if price < BUY_PRICE:
    print("wow!")
#     with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
#         connection.starttls()
#         connection.login(my_email,my_password)
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs=my_email,
#             msg=f"Subject:Rice Cooka on sale bud!\n\nBuy now!"
#         )
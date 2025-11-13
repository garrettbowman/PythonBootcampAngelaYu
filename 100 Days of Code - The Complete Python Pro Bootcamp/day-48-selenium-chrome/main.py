from re import search

from pytz.tzfile import build_tzinfo
from selenium import webdriver
from selenium.webdriver.common.by import By


#keep open after it finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
# driver.get("https://www.amazon.com/Housewares-cooked-Cooker-ARC-363NG-uncook/dp/B00N9N6GOY/ref=sr_1_3?crid=1ASZEEJ2YRM7R&dib=eyJ2IjoiMSJ9.PZKwy2ozyhUCDfrXi2cvyioWI2s8rxA0UaJ8HVyAmcgeStpKxmB1nNh_99CMnIk8BXw2hr5NdZEoBOBAguW_nY4Ah2B-4eJudHQs-UDm-yx0eT4V82be9m5CTM8lnxdlaCbT9jXi-6vFKkWqUFT5OROBJCC36PJYXDKOLquPyj-GSRD2AGssqwWeC9GikYVuQfTXi3xSUa5Nt0FL25vFwA4x3knHqRGvM0cGZaUHDFU.RJ6FBYhE9ejzUQ7M2-f0CivJMX2S1RMRJqCAJzoLEWk&dib_tag=se&keywords=rice%2Bcooker&qid=1762983397&sprefix=rice%2Bcooker%2Caps%2C313&sr=8-3&th=1")
driver.get("https://www.python.org")

# price_dollar = driver.find_element(By.CLASS_NAME,value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME,value="a-price-fraction")
# price = float(f"{price_dollar.text}.{price_cents.text}")
# print(price)

# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar)
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value= ".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[1]/div/ul/li[3]/a')
# print(bug_link.text)

driver.find_elements(By.CSS_SELECTOR,"")


# driver.close()
# whole browser
# driver.quit()
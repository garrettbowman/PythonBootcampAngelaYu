from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
# driver.get("https://www.amazon.com/Housewares-cooked-Cooker-ARC-363NG-uncook/dp/B00N9N6GOY/ref=sr_1_3?crid=1ASZEEJ2YRM7R&dib=eyJ2IjoiMSJ9.PZKwy2ozyhUCDfrXi2cvyioWI2s8rxA0UaJ8HVyAmcgeStpKxmB1nNh_99CMnIk8BXw2hr5NdZEoBOBAguW_nY4Ah2B-4eJudHQs-UDm-yx0eT4V82be9m5CTM8lnxdlaCbT9jXi-6vFKkWqUFT5OROBJCC36PJYXDKOLquPyj-GSRD2AGssqwWeC9GikYVuQfTXi3xSUa5Nt0FL25vFwA4x3knHqRGvM0cGZaUHDFU.RJ6FBYhE9ejzUQ7M2-f0CivJMX2S1RMRJqCAJzoLEWk&dib_tag=se&keywords=rice%2Bcooker&qid=1762983397&sprefix=rice%2Bcooker%2Caps%2C313&sr=8-3&th=1")
driver.get("https://www.python.org")

# dates = driver.find_elements(By.TAG_NAME,value="time")
event_dates = driver.find_elements(By.CSS_SELECTOR,value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR,value=".event-widget li a")
events ={}
for date in range(0,len(event_dates)):
    print(f"{event_dates[date].text} {event_names[date].text}")
    events[date] = {
        "time":event_dates[date].text,
        "name":event_names[date].text
    }
print(events)
# driver.close()
# whole browser
# driver.quit()
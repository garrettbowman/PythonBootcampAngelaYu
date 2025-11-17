from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate game page
driver.get("https://ozh.github.io/cookieclicker/")


time_up= False

time.sleep(5)
lang_EN = driver.find_element(By.ID, value="langSelect-EN")
lang_EN.click()

time.sleep(2)
big_cookie = driver.find_element(By.ID, value="bigCookie")
counter = 0
while not time_up:
    big_cookie.click()
    counter +=1
    if counter %200 ==0:

        rewards = driver.find_elements(By.CLASS_NAME,"enabled")
        try:
            rewards[-1].click()
        except:
            pass

    elif counter % 5000 ==0 :
        ps = driver.find_element(By.ID,"cookiesPerSecond")
        print(ps.text)
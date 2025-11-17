from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

inputs = driver.find_elements(By.CSS_SELECTOR, "form input")
inputs[0].send_keys("Gary")
inputs[1].send_keys("bo")
inputs[2].send_keys("Gary@asda.com")
button = driver.find_element(By.CSS_SELECTOR, "form button")

button.click()
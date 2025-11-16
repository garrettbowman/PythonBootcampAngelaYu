from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

numbers = driver.find_elements(By.CSS_SELECTOR, "#articlecount ul li a")
for n in numbers:
    print(n.text)

print(numbers[1].text.split(" ")[0])

# numbers[1].click()

all_portals = driver.find_element(By.LINK_TEXT,"Content portals")

# all_portals.click()
random_button = driver.find_element(By.CLASS_NAME,"search-toggle")
random_button.click()
search = driver.find_element(By.NAME,"search")
search.send_keys("python")
search.send_keys(Keys.ENTER)
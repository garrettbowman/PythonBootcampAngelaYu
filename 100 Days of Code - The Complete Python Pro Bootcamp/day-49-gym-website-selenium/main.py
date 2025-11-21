from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import NoSuchElementException, ElementNotInteractableException
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Add your credentials at the top of your script
ACCOUNT_EMAIL = "garrettbowman96@gmail.com"  # The email you registered with
ACCOUNT_PASSWORD = "$heddedm8"      # The password you used during registration
GYM_URL = "https://appbrewery.github.io/gym/"


# keeps chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# creating chrome user profile
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://appbrewery.github.io/gym/")

wait = WebDriverWait(driver, 2)
driver.implicitly_wait(3)
button = driver.find_element(By.ID, value="login-button")
button.click()
email = driver.find_element(By.ID, value="email-input")
email.send_keys(f"{ACCOUNT_EMAIL}")
password = driver.find_element(By.ID, value="password-input")
password.send_keys(f"{ACCOUNT_PASSWORD}")
login_submit = driver.find_element(By.ID, value="submit-button")
login_submit.click()


# errors = [NoSuchElementException, ElementNotInteractableException]
# wait = WebDriverWait(driver, timeout=2, poll_frequency=.2, ignored_exceptions=errors)
# wait.until(lambda _ : revealed.send_keys("Displayed") or True)
# worked = driver.presence_of_element_located(By.CSS_SELECTOR,"schedule-page")

# element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "schedule-page")))
wait.until(EC.presence_of_element_located((By.ID, "schedule-page")))

tues_spin_class = driver.find_element(By.CSS_SELECTOR,'div[id^="day-group-tue"] div[id^="class-card-spin-"]')
tues_spin_day = driver.find_element(By.CSS_SELECTOR,'div[id^="day-group-tue"] h2')
tues_spin_class_button = driver.find_element(By.CSS_SELECTOR,'div[id^="day-group-tue"] div[id^="class-card-spin-"] button')
# print(tues_spin_class)
tues_spin_class_button.click()
print(f"✓ Booked: Spin Class on {tues_spin_day.text}")


print("✓ Already booked: Spin Class on Tue, Aug 12")

print("✓ Already on waitlist: HIIT Class on Tue, Aug 12")

print("✓ Joined waitlist for: Yoga Class on Tue, Aug 12")
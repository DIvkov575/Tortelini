import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_driver_path = "./chromedriver"
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Open browser in maximized mode
chrome_options.add_argument("--disable-infobars")  # Disable info bars
chrome_options.add_argument("--disable-extensions")  # Disable extensions

service = Service(chrome_driver_path)  # Create a Service instance with the path to ChromeDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://accounts.google.com/signin")

# signup button
driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[3]/div/div[2]/div/div/div[1]/div/button').click()
# "for personal use option"
driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[3]/div/div[2]/div/div/div[2]/div/ul/li[1]').click()

try:
    username_input = driver.find_element(By.CSS_SELECTOR, "input#firstName")
    username_input.send_keys("askjdf")
    username_input = driver.find_element(By.CSS_SELECTOR, "input#lastName")
    username_input.send_keys(";kl")
except Exception:
    pass


# continue button
driver.find_element(By.XPATH, '//*[@id="collectNameNext"]/div/button').click()

# fill out age/gender
try:
    time.sleep(1)
    elem = driver.find_element(By.CSS_SELECTOR, "#year")
    elem.send_keys("2000")
    elem = driver.find_element(By.CSS_SELECTOR, "#day")
    elem.send_keys("13")
    driver.find_element(By.CSS_SELECTOR, "#month > option:nth-child(3)").click()
    driver.find_element(By.CSS_SELECTOR, "#gender> option:nth-child(3)").click()
except Exception as e:
    pass

# continue button
driver.find_element(By.CSS_SELECTOR, '#birthdaygenderNext > div > button').click()

# select first suggested email option
try:

    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div/div/form/span/section/div/div/div[1]/div[1]/div/span/div[1]/div/div[1]/div/div[3]').click()

except Exception as e:
    print(e)

# continue button
driver.find_element(By.CSS_SELECTOR, '#next > div > button').click()



time.sleep(180)

driver.quit()
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

driver.get("https://example.com")

time.sleep(25)
print("Page title:", driver.title)
driver.quit()
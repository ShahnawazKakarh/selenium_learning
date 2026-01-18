import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# <a is a link type. We will use linktext on such cases.

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client//")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()

# partial link text
# driver.find_element(By.PARTIAL_LINK_TEXT, "password?").click()

# css-selector - tagname[attribute='value']
driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("<PASSWORD>")

time.sleep(30)

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client/")

driver.find_element(By.CSS_SELECTOR, "input[id='userEmail']").send_keys("hmm@gmail.com")
driver.find_element(By.CSS_SELECTOR, "input[id='userPassword']").send_keys("A#Sd1234567")
driver.find_element(By.CSS_SELECTOR, "input[value='Login']").click()

time.sleep(30)

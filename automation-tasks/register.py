import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client/")
driver.find_element(By.CSS_SELECTOR, ".text-reset").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "input[id='firstName']").send_keys("KAKS")
driver.find_element(By.CSS_SELECTOR, "input[id='lastName']").send_keys("BAGS")
driver.find_element(By.CSS_SELECTOR, "input[id='userEmail']").send_keys("hmm@gmail.com")
driver.find_element(By.CSS_SELECTOR, "input[id='userMobile']").send_keys("2345671234")
driver.find_element(By.CSS_SELECTOR, "input[value='Male']").click()
driver.find_element(By.CSS_SELECTOR, "input[id='userPassword']").send_keys("A#Sd1234567")
driver.find_element(By.CSS_SELECTOR, "input[id='confirmPassword']").send_keys("A#Sd1234567")
driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']").click()
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
# Account Created Successfully
time.sleep(10)

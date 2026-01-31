import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client/#/auth/login")

driver.find_element(By.XPATH, "//input[@formcontrolname='userEmail']").send_keys("bagskaks@gmail.com")
driver.find_element(By.XPATH, "//input[@formcontrolname='userPassword']").send_keys("Abcdefg")
driver.find_element(By.XPATH, "//input[@type='submit']").click()

time.sleep(15)

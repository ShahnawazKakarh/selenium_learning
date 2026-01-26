import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client/#/auth/login")

driver.find_element(By.XPATH, "//a[@class='btn1']").click()
driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys('hurrah')
driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys('ali')
driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys('hurrah@gmail.com')
driver.find_element(By.XPATH, "//input[@id='userMobile']").send_keys('3001234567')
driver.find_element(By.XPATH, "//input[@value='Male']").click()
driver.find_element(By.XPATH, "//input[@formcontrolname='userPassword']").send_keys('Ibrahim1')
driver.find_element(By.XPATH, "//input[@formcontrolname='confirmPassword']").send_keys('Ibrahim1')
driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()

time.sleep(25)

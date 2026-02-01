import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

name = "KAKARH"

# ALERT BOX POP UP
driver.find_element(By.XPATH, "//fieldset/input[@name='enter-name']").send_keys(name)

# CLICK ON ALERT BUTTON SO POP UP CAN APPEAR
driver.find_element(By.XPATH, "//fieldset/input[@id='alertbtn']").click()

alert = driver.switch_to.alert
alertText = alert.text
print(alertText)

assert name in alertText

# Click on OK on POP UP
alert.accept()
time.sleep(2)

# Clicking on POP-UP with both OK and CANCEL option
driver.find_element(By.XPATH, "//fieldset/input[@id='confirmbtn']").click()

# to click on pop-up cancel button
alert.dismiss()

time.sleep(10)

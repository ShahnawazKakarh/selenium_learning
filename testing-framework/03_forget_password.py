import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client/#/auth/login")

# Redirecting to Forgot Password >> Using XPATH
# driver.find_element(By.XPATH, "//a[@class='forgot-password-link']").click()
# driver.find_element(By.XPATH, "//input[@formcontrolname='userEmail']").send_keys("hurrah@gmail.com")
# driver.find_element(By.XPATH, "//input[@formcontrolname='userPassword']").send_keys("Abcdefg")
# driver.find_element(By.XPATH, "//input[@formcontrolname='confirmPassword']").send_keys("Abcdefg")
# driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Redirecting to Forgot Password >> Using LinkText
driver.find_element(By.LINK_TEXT, "Forgot Password").click()

# Selectors using custom CSS-SELECTORS and XPATH Elements
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("hurrah@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Abcdefg")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(3) input").send_keys("Abcdefg")
driver.find_element(By.XPATH, "//button[text()='Save New Password").click()

time.sleep(15)

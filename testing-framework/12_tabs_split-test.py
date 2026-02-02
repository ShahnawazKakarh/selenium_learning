from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

# IMPLICIT WAIT
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()

tabsOpened = driver.window_handles
driver.switch_to.window(tabsOpened[1])

text = driver.find_element(By.XPATH, "//div/p[@class='im-para red']").text
emailText = text.split(" at ")[1].split()[0]
print(emailText)

driver.switch_to.window(tabsOpened[0])

textIncorrect = "Incorrect username/password."
# //*[@id="login-form"]/div[1]/text()

driver.find_element(By.NAME, "username").send_keys(emailText)
driver.find_element(By.NAME, "password").send_keys('emailText')
driver.find_element(By.XPATH, "//*[@id='login-form']/div[5]/select/option[1]")
driver.find_element(By.XPATH, "//*[@id='terms']").click()
driver.find_element(By.XPATH, "//*[@id='signInBtn']")

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
incorrectText = driver.find_element(By.CSS_SELECTOR, ".alert-danger").text
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)

assert textIncorrect == incorrectText

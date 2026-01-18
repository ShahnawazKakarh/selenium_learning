import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

# locators class, classname, name, xpath, linkText etc
# driver.find_element(By.NAME, "name").send_keys("John Albert")
driver.find_element(By.NAME, "email").send_keys("demo@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("demo@com")
driver.find_element(By.ID, "exampleCheck1").click()

# xpath - //tagname[@attribute='value']
# //input[@type='submit']
driver.find_element(By.XPATH, "//input[@type='submit']").click()

success_message = "Success! The Form has been submitted successfully!."
form_success_message = driver.find_element(By.CLASS_NAME, "alert-success").text
assert success_message in form_success_message
assert "Success!" in form_success_message

# css-selector - tagname[attribute='value']
# input[attribute='name']
# .classname
# #id
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("John Cena")
driver.find_element(By.CSS_SELECTOR, "input[value='option1']").click()
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hello World")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

# webpage_title
webpage_title = driver.title
print(webpage_title)

# webpage_current_url
webpage_current_url = driver.current_url
print(webpage_current_url)

time.sleep(30)

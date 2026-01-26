import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# We can use manually or direct chrome, firefox etc service
driver = webdriver.Chrome()
# chrome_service = Service('/Users/shahnawazkhan/Downloads/chromedriver-mac-arm64/chromedriver')
# driver = webdriver.Chrome(service=chrome_service)

driver.get("https://rahulshettyacademy.com/angularpractice")
driver.maximize_window()
# print(driver.title)
# print(driver.current_url)

# locators id, name, linkText, partial-linkText
driver.find_element(By.NAME, "name").send_keys("John Albert")
driver.find_element(By.NAME, "email").send_keys("demo@localhost.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("localhost")

# Checkbox: Check me out if you Love IceCreams!
driver.find_element(By.ID, "exampleCheck1").click()

# Selecting Static Value from DropDown
select = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
select.select_by_visible_text("Male")
# select.select_by_visible_text("Female")
# select.select_by_index(1)

# LOCATORS USING XPATH
# We can Write Locators as  >>>>> //tagname[@attribute='value']
# HTML Element >>>>> <input class="btn btn-success" type="submit" value="Submit">
# 'input' is >> tagname,
# 'class', 'type', 'value' is >> attribute

# //input[@class='btn btn-success']
# //input[@type='submit']
# //input[@value='submit']

# LOCATORS USING CSS SELECTORS [WAY 1]
# We can Write Locators as  >>>>> tagname[attribute='value']
# HTML Element >>>>>
# <input class="form-control ng-pristine ng-invalid ng-touched" minlength="2" name="name" required="" type="text">
# input[class='ng-touched']
# input[type='text']
# input[name='name']

# LOCATORS USING CSS SELECTORS [WAY 2]
# #id
# .class-name

# Employment Status
driver.find_element(By.CSS_SELECTOR, "input[value='option2']").click()

# Click Submit Button
driver.find_element(By.XPATH, "//input[@class='btn btn-success']").click()

# Asserting Success Message on Submit Button click
success_message = "Success! The Form has been submitted successfully!."
message = driver.find_element(By.CLASS_NAME, "alert-success").text
assert 'Success' in success_message

driver.find_element(By.XPATH, "(//input[@name='name'])[2]").send_keys('Finally')

time.sleep(30)

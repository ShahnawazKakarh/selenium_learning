import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise")

driver.find_element(By.XPATH, "//input[@id='autosuggest']").send_keys("ind")
time.sleep(2)

# Different ways to extract WEB ELEMENTS using XPATH and CSS SELECTOR
# countries = driver.find_elements(By.XPATH, "//ul/li[@class='ui-menu-item']/a")
# countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
countries = driver.find_elements(By.XPATH, "//ul/li[@class='ui-menu-item']")

len(countries)
for country in countries:
    if country.text == 'India':
        country.click()
        break

# If the value is static and not changed in HTML script, we can retrieve it using .text()
# print(driver.find_element(By.XPATH, "//input[@id='autosuggest']").text)

# If the value is dynamically changed in HTML script, we can retrieve it from DOM using 'get_attribute' method
# print(driver.find_element(By.XPATH, "//input[@id='autosuggest']").get_attribute("value"))
assert driver.find_element(By.XPATH, "//input[@id='autosuggest']").get_attribute("value") == "India"

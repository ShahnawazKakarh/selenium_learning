import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)  # IMPLICIT WAIT

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

promo_code = "rahulshettyacademy"
driver.find_element(By.CSS_SELECTOR, "div input[type='search']").send_keys("ber")
# driver.find_element(By.XPATH, "//div//input[@type='search']")
# driver.find_element(By.CLASS_NAME, ".search-keyword")

# Added time as it is finding multiple number of records.
time.sleep(3)
products = driver.find_elements(By.XPATH, "//div[@class='products']/div")  # LIST
count = len(products)
assert count > 0

for product in products:
    product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.XPATH, "//div/input[@class='promoCode']").send_keys(promo_code)
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
code_applied = (driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)
print(code_applied)
assert 'Code applied ..!' in code_applied

# EXPLICIT WAIT
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
driver.find_element(By.XPATH, "//button[normalize-space()='Place Order']").click()

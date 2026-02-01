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

product_list = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actual_list = []

for product in products:
    actual_list.append(product.find_element(By.XPATH, "h4").text)
    product.find_element(By.XPATH, "div/button").click()

print(actual_list)
assert product_list == actual_list

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

# FUNCTIONAL TEST CASES ADDING:
# Here are different ways of finding XPATH and CSS SELECTORS
# driver.find_element(By.XPATH, "//tr/td[5]/p[@class='amount']")
# driver.find_element(By.XPATH, "//tr/td[5]/p")
# driver.find_element(By.XPATH, "//td[5]/p")
# driver.find_element(By.CSS_SELECTOR, "tr td:nth-child(5) p[class='amount'] p")
# driver.find_element(By.CSS_SELECTOR, "tr td:nth-child(5) p")
# driver.find_element(By.CSS_SELECTOR, "td:nth-child(5) p")

# Addition of Prices and its validation
pricesList = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in pricesList:
    sum = sum + int(price.text)

totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum == totalAmount

discountAmt = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
assert discountAmt <= sum

print(sum)
print(discountAmt)

driver.find_element(By.XPATH, "//button[normalize-space()='Place Order']").click()

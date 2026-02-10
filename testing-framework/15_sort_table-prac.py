from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')

# IMPLICIT WAIT
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.LINK_TEXT, "Top Deals").click()

tabsOpened = driver.window_handles
driver.switch_to.window(tabsOpened[1])
driver.maximize_window()

# driver.find_element(By.XPATH, "//th[1]").click()
driver.find_element(By.XPATH, "//th[@aria-sort='descending']").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//th[@aria-sort='ascending']")))

# sorted_list = ['Almond', 'Apple', 'Banana', 'Beans', 'Brinjal']
sorted_list = []

veggie_web = driver.find_elements(By.XPATH, "//tr/td[1]")
for veggie in veggie_web:
    sorted_list.append(veggie.text)

    assert veggie.text in sorted_list

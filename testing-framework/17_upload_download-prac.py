from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/upload-download-test/")

# IMPLICIT WAIT
driver.implicitly_wait(5)

file_path = "/Volumes/Home/python/selenium_learning/extra-files/excel-files/download.xlsx"
# Step 1: Download the file
# driver.find_element(By.CLASS_NAME, ".button").click()
driver.find_element(By.ID, "downloadButton").click()

# Step 2: Edit the Excel File
# Right now doing Manually

# Step 3: Upload the Excel file
# for it there should be web element type="file"
file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
file_input.send_keys(file_path)

wait = WebDriverWait(driver, 5)
toaster_locator = (By.CSS_SELECTOR, ".Toastify__toast-body div:nth-child(2)")
wait.until(expected_conditions.visibility_of_element_located(toaster_locator))
print(driver.find_element(*toaster_locator).text)

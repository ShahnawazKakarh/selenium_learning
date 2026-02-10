from selenium import webdriver

driver = webdriver.Chrome()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument('--ignore-certificate-errors')

# IMPLICIT WAIT
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# Scroll to specific Range
# driver.execute_script("window.scrollTo(0,600)")

# Scroll Full Web Page to Down
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
driver.get_screenshot_as_file("scroll.png")

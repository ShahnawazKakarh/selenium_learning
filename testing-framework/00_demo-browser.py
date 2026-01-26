import time

from selenium import webdriver

# We can use manually or direct chrome, firefox etc service
driver = webdriver.Chrome()
# chrome_service = Service('/Users/shahnawazkhan/Downloads/chromedriver-mac-arm64/chromedriver')
# driver = webdriver.Chrome(service=chrome_service)

driver.get("http://rahulshettyacademy.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

time.sleep(50)

import time

from selenium import webdriver

# if we want to call chrome driver manually
# from selenium.webdriver.chrome.service import Service
# service_obj = Service("C:\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://www.google.com")

# calling webdriver without manual Chrome version
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()

# webpage_title
webpage_title = driver.title
print(webpage_title)

# webpage_current_url
webpage_current_url = driver.current_url
print(webpage_current_url)

time.sleep(3)

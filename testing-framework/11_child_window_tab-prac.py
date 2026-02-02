from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# IMPLICIT WAIT
driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
new_window_text = "New Window"
open_new_window_text = "Opening a new window"

driver.find_element(By.LINK_TEXT, "Click Here").click()
textNewWindow = driver.find_element(By.XPATH, "//div/h3")
assert open_new_window_text == textNewWindow.text

tabsOpened = driver.window_handles
driver.switch_to.window(tabsOpened[1])

new_window_text_extracted = driver.find_element(By.XPATH, "//div/h3")
# text_extracted = driver.find_element(By.TAG_NAME, "h3")
assert new_window_text == new_window_text_extracted.text
driver.close()

# Switching back to window [0] from window [1]
driver.switch_to.window(tabsOpened[0])
textAgainNewWindow = driver.find_element(By.XPATH, "//div/h3")
assert open_new_window_text == textAgainNewWindow.text

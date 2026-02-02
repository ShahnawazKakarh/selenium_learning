from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# IMPLICIT WAIT
driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()
driver.find_element(By.XPATH, "//div[@class='tox-icon']").click()

textTitle = 'An iFrame containing the TinyMCE WYSIWYG Editor'
textExtracted = driver.find_element(By.CSS_SELECTOR, "h3").text
print(textExtracted)

assert textTitle in textExtracted

driver.switch_to.frame('mce_0_ifr')
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys('I cannot write here')

driver.switch_to.default_content()
textExtracted = driver.find_element(By.CSS_SELECTOR, "h3").text
assert textTitle in textExtracted

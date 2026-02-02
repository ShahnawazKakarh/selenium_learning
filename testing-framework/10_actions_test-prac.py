from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# IMPLICIT WAIT
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
# time.sleep(3)
# driver.find_elements(By.XPATH, '//*[@id="content"]')


# EXPLICIT WAIT
# wait = WebDriverWait(driver, 10)
# wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".")))

# ACTION CLASS TESTING
action = ActionChains(driver)
action.click_and_hold()
action.double_click()
action.context_click()
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).perform()

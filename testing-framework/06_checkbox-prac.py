import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Select CheckBox OPTION 2
# driver.find_element(By.XPATH, "//label/input[@id='checkBoxOption2']").click()

# Select RadioButton OPTION 2
# driver.find_element(By.XPATH, "//label/input[@value='radio2']").click()

# If we want to click on specific radio button we can do by extracting all and then choosing the specific one by index
# radioButtons = driver.find_element(By.CSS_SELECTOR, ".radioButton")
# radioButtons[2].click()
# assert radioButtons[2].is_selected()

# Check BOX Options selected
checkBoxOptions = driver.find_elements(By.XPATH, "//label/input[@type='checkbox']")

# Print Length of total CheckBoxes
print(len(checkBoxOptions))

# Extracting all CheckBox Options and iterate with the specific one
for checkBoxOption in checkBoxOptions:
    if checkBoxOption.get_attribute("value") == "option2":
        checkBoxOption.click()
        checkBoxOption.is_selected()
        break

# RADIO BUTTON selected
radioButtons = driver.find_elements(By.XPATH, "//label/input[@type='radio']")

# Print Length of total Radio Buttons
print(len(radioButtons))

# Extracting all Radio Buttons and iterate with the specific one
for radioButton in radioButtons:
    if radioButton.get_attribute("value") == "radio2":
        radioButton.click()
        radioButton.is_selected()
        break

# BOX will be displayed
displayed_box = driver.find_element(By.XPATH, "//fieldset/input[@id='displayed-text']")
# displayed_box = driver.find_element(By.ID, "displayed-text")

# Now box will be hide
driver.find_element(By.ID, "hide-textbox").click()

# Assertion that box is not displayed
assert not displayed_box.is_displayed()


time.sleep(10)

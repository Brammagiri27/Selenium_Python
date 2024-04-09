import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service = service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH , "//input[@type='checkbox']")
print(len(checkboxes))
# get_attribute("attribute")
for checkbox in checkboxes:
    if checkbox.get_attribute("id") == "checkBoxOption2" :
        checkbox.click()
        break
time.sleep(3)





import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME , "name").send_keys("Brammagiri G")
driver.find_element(By.XPATH , "//input[@name='email']").send_keys("giri27121999@gmail.com")
driver.find_element(By.XPATH , "//input[@type='password']").send_keys("hello123")
driver.find_element(By.CSS_SELECTOR , "#exampleCheck1").click()
# Static Dropdown -- Use Select Class

dropdown = Select(driver.find_element(By.XPATH , "//select[@id='exampleFormControlSelect1']"))
dropdown.select_by_index(0)
dropdown.select_by_visible_text("Male")
# RadioButton

driver.find_element(By.CSS_SELECTOR , "#inlineRadio1").click()
driver.find_element(By.XPATH , "//input[@type='date']").send_keys(12121999)

# If there are multiple elements while creating XPATH use () for whole xpath followed by [index]
driver.find_element(By.XPATH , "(//input[@type='text'])[3]").clear()
driver.find_element(By.XPATH , "(//input[@type='text'])[3]").send_keys("GiriRS45")
driver.find_element(By.XPATH , "//input[@type='submit']").click()


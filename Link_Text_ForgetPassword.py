import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/client")
# Creating XPATH from Parent to child element
# Syntax -- //parent/child[index]/child
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.XPATH, "//form/div[2]/input").send_keys("123456")
driver.find_element(By.XPATH , "//input[@value='Login']").click()
driver.find_element(By.LINK_TEXT , "Forgot password?").click()
time.sleep(3)
driver.find_element(By.XPATH , "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.XPATH , "//form/div[2]/input").send_keys("123456")
driver.find_element(By.XPATH , "//form/div[3]/input").send_keys("123456")
driver.find_element(By.XPATH , "//form/div[4]/button").click()
time.sleep(3)
driver.close()
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/locatorspractice/")


# Find element by ID -- By providing Attribute value of the ID
driver.find_element(By.ID , "inputUsername").send_keys("giri27121999@gmail.com")
# Find element by Name --- By providing the Attribute value of the name
driver.find_element(By.NAME,"inputPassword").send_keys("Brammagiri123")
# Find the element by XPATH
#Syntax --- //tagname[@attributename = 'attributevalue']
driver.find_element(By.XPATH, "//input[@id='chkboxOne']").click()
driver.find_element(By.ID ,"chkboxTwo").click()
driver.find_element(By.XPATH, "//button[@class='submit signInBtn']").click()
time.sleep(8)
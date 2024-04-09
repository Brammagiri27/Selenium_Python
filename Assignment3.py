from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service = service_obj)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.CSS_SELECTOR , ".blinkingText").click()
OpenedWindows = driver.window_handles

driver.switch_to.window(OpenedWindows[1])
message = driver.find_element(By.XPATH , "//div/p[@class='im-para red']").text
print(message)
var = message.split("at")[1].strip().split(" ")
print(var)
driver.switch_to.window(OpenedWindows[0])
driver.find_element(By.ID , "username").send_keys(var[0])
driver.find_element(By.ID , "password").send_keys("BrammagiriG")
driver.find_element(By.XPATH , "//label[@class='customradio'][1]").click()
# driver.find_element(By.XPATH , "//div/button[@class='btn btn-success']").click()
driver.find_element(By.XPATH , "//input[@type='checkbox']").click()
driver.find_element(By.ID , "signInBtn").click()

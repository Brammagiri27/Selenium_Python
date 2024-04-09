import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

# Implicit Wait
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.XPATH , "//input[@type='search']").send_keys("ber")
results = driver.find_elements(By.XPATH , "//div[@class='product']")
count = len(results)
assert count > 0
for result in results:
    result.find_element(By.XPATH, "//div[@class='products']/div/div/button").click()

driver.find_element(By.XPATH , "//img[@alt='Cart']").click()
driver.find_element(By.XPATH , "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.XPATH, "//input[@placeholder='Enter promo code']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[@class='promoBtn']").click()

# Explicit Wait
wait = WebDriverWait(driver , 15)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR , ".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR , ".promoInfo").text)
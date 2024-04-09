# Compare using Assertion were Total Amount was always less than the Total After Discount


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
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
wait = WebDriverWait(driver , 15)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR , ".promoInfo")))
Total_Amount = int(driver.find_element((By.XPATH , "//span[@class='totAmt']").text))
Discounted_Amount = float(driver.find_element((By.XPATH , "//span[@class='discountAmt']").text))

assert Total_Amount > Discounted_Amount
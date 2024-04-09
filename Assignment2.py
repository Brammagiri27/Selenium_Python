from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service()
driver = webdriver.Chrome(service = service_obj)
ExpectedList = ['Cucumber - 1 Kg' , 'Raspberry - 1/4 Kg' , 'Strawberry - 1/4 Kg']
ActualList = []
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)
driver.find_element(By.XPATH , "//input[@type='search']").send_keys("ber")
results = driver.find_elements(By.XPATH , "//div[@class='product']")
count = len(results)
assert count > 0
for result in results:
    ActualList.append.(result.find_element(By.XPATH , "/div/h4").text)
    result.find_element(By.XPATH , "//div[@class='products']/div/div/button").click()

driver.find_element(By.XPATH , "//img[@alt='Cart']").click()
driver.find_element(By.XPATH , "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.XPATH , "//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH , "//button[@class='promoBtn']").click()
wait = WebDriverWait(driver , 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH , "//span[@class='promoInfo']")))
print(driver.find_element(By.XPATH , "//span[@class='promoInfo']").text)

# assert ActualList == ExpectedList




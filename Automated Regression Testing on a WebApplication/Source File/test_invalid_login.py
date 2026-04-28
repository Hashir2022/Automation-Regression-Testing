from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com")
time.sleep(3)

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("wrongpass")

driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(3)

driver.save_screenshot("Step5_Error.png")

print("INVALID LOGIN TEST EXECUTED")


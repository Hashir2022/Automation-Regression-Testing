from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
# Open website
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
print("Website opened - now manually observe and enter data if needed")

# Wait so user can SEE and interact manually
time.sleep(3)

# OPTIONAL: You can manually enter during this time

# Screenshot before login
driver.save_screenshot("manual_step1.png")

input("After entering data manually, press ENTER to continue...")

# Click login manually OR via code
try:
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
except:
    print("Login already done manually")
time.sleep(3)
driver.save_screenshot("manual_step2_dashboard.png")
print("Manual test completed")

driver.quit()
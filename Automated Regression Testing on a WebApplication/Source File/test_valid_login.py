from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# STEP 1: Open website
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
time.sleep(3)

driver.save_screenshot("Step1_Open.png")

# STEP 2: Username
driver.find_element(By.NAME, "username").send_keys("Admin")
time.sleep(2)
driver.save_screenshot("Step2_Username.png")

# STEP 3: Password
driver.find_element(By.NAME, "password").send_keys("admin123")
time.sleep(2)
driver.save_screenshot("Step3_Password.png")

# STEP 4: Login click
time.sleep(2)
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# STEP 5: Dashboard wait
time.sleep(5)
driver.save_screenshot("Step4_Dashboard.png")

# ✅ DASHBOARD CHECK
try:
    dashboard = driver.find_element(By.XPATH, "//h6[text()='Dashboard']")
    if dashboard.is_displayed():
        print("DASHBOARD LOADED SUCCESSFULLY ✅")
except:
    print("DASHBOARD NOT FOUND ❌")

# ✅ SIDE MENU CHECK (NEW IMPORTANT PART)
try:
    side_menu = driver.find_element(By.CLASS_NAME, "oxd-sidepanel")
    if side_menu.is_displayed():
        print("SIDE MENU IS VISIBLE & OPENED ✅")
    else:
        print("SIDE MENU NOT VISIBLE ❌")
except:
    print("SIDE MENU TEST FAILED ❌")

# FINAL PAUSE FOR VIDEO
time.sleep(3)
input("Press ENTER to close browser...")
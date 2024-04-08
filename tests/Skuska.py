import time

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.opencart.com/")
time.sleep(5)
driver.find_element(By.XPATH, "//span[contains(text(), 'My Account')]").click()
driver.find_element(By.LINK_TEXT, "Login").click()

wait = WebDriverWait(driver, 10)
email_field = wait.until(expected_conditions.visibility_of_element_located(driver.find_element(By.ID, "input-email").send_keys("b")))

driver.find_element(By.ID, "input-password").send_keys("12345")
time.sleep(5)
driver.find_element(By.XPATH, "//button[@type= 'submit']").click()
    # # expected_warning = "Warning: No match for E-Mail Address and/or Password."
    # time.sleep(5)
    # print(driver.title)
    # # print(driver.find_element(By.XPATH,"//div[@id= 'alert']/div").text)
print("OK")
time.sleep(3)
driver.quit()


# def generate_email_with_time_stamp():
#     timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
#     timestamp = timestamp.replace("-", "_").replace(" ", "_").replace(":", "_")
#     return "anicka"+timestamp+"@gmail.com"

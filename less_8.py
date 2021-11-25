from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")

    elements = browser.find_elements(By.CSS_SELECTOR, "input")
    print(len(elements))

    for element in elements:
        element.send_keys("Test")

    browser.find_element(By.XPATH, "//button[@type='submit']").click()

finally:
    time.sleep(30)
    browser.close()
    browser.quit()

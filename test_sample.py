import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def test_tutorials_ninja():
    ser_obj = Service("C:/Driver/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=ser_obj)
    driver.maximize_window()
    time.sleep(3)
    driver.get("https://tutorialsninja.com/demo/")
    time.sleep(3)
    expected_title="Your Store"
    actual_title=driver.title
    assert actual_title.__eq__(expected_title)
    driver.find_element(By.XPATH,"//*[@id='search']/input").send_keys("HP")
    time.sleep(2)
    driver.find_element(By.XPATH,"//*[@id='search']/span/button").click()
    time.sleep(3)
    assert driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()
    driver.quit()

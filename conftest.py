import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup_and_teardown(request):
    ser_obj = Service("C:/Driver/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=ser_obj)
    driver.get("https://tutorialsninja.com/demo/")
    time.sleep(4)
    driver.maximize_window()
    time.sleep(5)
    request.cls.driver=driver
    yield
    driver.quit()
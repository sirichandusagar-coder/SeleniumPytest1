import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    @allure.severity(allure.severity_level.CRITICAL)
    def test_tutorials_ninja(self):
        self.driver.find_element(By.XPATH,"//*[@id='search']/input").send_keys("HP")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//*[@id='search']/span/button").click()
        time.sleep(3)
        assert self.driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()

    @allure.severity(allure.severity_level.MINOR)
    def test_search_entering_invalid_data(self):
        self.driver.find_element(By.XPATH, "//*[@id='search']/input").send_keys("Honda")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='search']/span/button").click()
        time.sleep(3)
        expected_text = "There is no product that matches the search criteria."
        assert self.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)

    @allure.severity(allure.severity_level.TRIVIAL)
    def test_search_without_entering_anything(self):
          self.driver.find_element(By.XPATH, "//*[@id='search']/input").send_keys("")
          time.sleep(2)
          self.driver.find_element(By.XPATH, "//*[@id='search']/span/button").click()
          time.sleep(3)
          expected_text = "There is no product that matches the search criteria."
          assert self.driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)
          allure.attach(self.driver.get_screenshot_as_png(),name="without_providing_data",attachment_type=AttachmentType.PNG)
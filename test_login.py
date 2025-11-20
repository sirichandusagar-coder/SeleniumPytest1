import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_login_with_valid_credentials(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        time.sleep(7)
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "input-email").send_keys("sirichandusagar@gmail.com")
        time.sleep(4)
        self.driver.find_element(By.ID, "input-password").send_keys("Tuffy@4517")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        time.sleep(4)
        assert self.driver.find_element(By.LINK_TEXT, "Edit your account information").is_displayed()


    def test_login_without_entering_credentials(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        time.sleep(7)
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "input-email").send_keys("")
        time.sleep(4)
        self.driver.find_element(By.ID, "input-password").send_keys("")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        time.sleep(4)
        expected_warning_message="Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH,"//div[@id='account-login']/div[1]").text.__contains__(expected_warning_message)

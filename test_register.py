
import time
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:
    def test_register_with_valid_credentials(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        time.sleep(7)
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "input-firstname").send_keys("chandana")
        time.sleep(3)
        self.driver.find_element(By.ID, "input-lastname").send_keys("HS")
        time.sleep(3)
        self.driver.find_element(By.ID, "input-email").send_keys(self.generate_email_time_stamp())
        time.sleep(3)
        self.driver.find_element(By.ID, "input-telephone").send_keys("1234567890")
        time.sleep(3)
        self.driver.find_element(By.ID, "input-password").send_keys("Tuffy@123")
        time.sleep(3)
        self.driver.find_element(By.ID, "input-confirm").send_keys("Tuffy@123")
        time.sleep(3)
        self.driver.find_element(By.NAME, "agree").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        time.sleep(3)
        expected_text="Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH,"//div[@id='content']/h1").text.__eq__(expected_text)

    def generate_email_time_stamp(self):
        raw_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        safe_timestamp = raw_timestamp.replace("-", "_").replace(":", "_").replace(" ", "_")
        return "chandana" + safe_timestamp + "@gmail.com"

    def test_create_account_by_allfields(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        time.sleep(7)
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "input-firstname").send_keys("chandana")
        time.sleep(3)
        self.driver.find_element(By.ID, "input-lastname").send_keys("HS")
        time.sleep(3)
        self.driver.find_element(By.ID, "input-email").send_keys(self.generate_email_time_stamp())
        time.sleep(3)
        self.driver.find_element(By.ID, "input-telephone").send_keys("1234567890")
        time.sleep(3)
        self.driver.find_element(By.ID, "input-password").send_keys("Tuffy@123")
        time.sleep(3)
        self.driver.find_element(By.ID, "input-confirm").send_keys("Tuffy@123")
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//*[@id='content']/form/fieldset[3]/div/div/label[1]/input").click()
        time.sleep(2)
        self.driver.find_element(By.NAME, "agree").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        time.sleep(3)
        expected_text = "Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(expected_text)

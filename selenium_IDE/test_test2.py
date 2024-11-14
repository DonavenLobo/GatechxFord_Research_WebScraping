# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTest2():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test2(self):
    self.driver.get("https://www.carfax.com/Used-Ford-Mustang-Mach-E-Atlanta-GA_w9809_c16158")
    self.driver.set_window_size(1550, 830)
    self.driver.find_element(By.CSS_SELECTOR, ".accordion > div:nth-child(1) .accordion_header").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'srp-filter-container\']/div[2]/div[3]/div[2]/div/details/div/div/div/div/select").click()
    dropdown = self.driver.find_element(By.XPATH, "//div[@id=\'srp-filter-container\']/div[2]/div[3]/div[2]/div/details/div/div/div/div/select")
    dropdown.find_element(By.XPATH, "//option[. = '50']").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'srp-filter-container\']/div[2]/div[3]/div[2]/div/details/div/div/div/div/select").click()
    dropdown = self.driver.find_element(By.XPATH, "//div[@id=\'srp-filter-container\']/div[2]/div[3]/div[2]/div/details/div/div/div/div/select")
    dropdown.find_element(By.XPATH, "//option[. = 'Unlimited']").click()
  
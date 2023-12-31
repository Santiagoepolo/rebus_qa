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

class TestBsquedasinresultado():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_bsquedasinresultado(self):
    self.driver.get("https://demowebshop.tricentis.com/")
    self.driver.set_window_size(1366, 728)
    self.driver.find_element(By.ID, "small-searchterms").click()
    self.driver.find_element(By.ID, "small-searchterms").send_keys("perejil")
    self.driver.find_element(By.CSS_SELECTOR, ".search-box-button").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "h1").text == "Search"
    assert self.driver.find_element(By.CSS_SELECTOR, ".result").text == "No products were found that matched your criteria."
    self.driver.close()
  

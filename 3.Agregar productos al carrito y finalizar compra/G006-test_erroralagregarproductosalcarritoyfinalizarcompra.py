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

class TestErroralagregarproductosalcarritoyfinalizarcompra():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_erroralagregarproductosalcarritoyfinalizarcompra(self):
    self.driver.get("https://demowebshop.tricentis.com/")
    self.driver.set_window_size(1366, 728)
    self.driver.find_element(By.LINK_TEXT, "Log in").click()
    self.driver.find_element(By.ID, "Email").click()
    self.driver.find_element(By.ID, "Email").send_keys("santiago97@hotmail.com")
    self.driver.find_element(By.ID, "Password").click()
    self.driver.find_element(By.ID, "Password").send_keys("qwertyuiop")
    self.driver.find_element(By.CSS_SELECTOR, ".login-button").click()
    self.driver.find_element(By.ID, "small-searchterms").click()
    self.driver.find_element(By.ID, "small-searchterms").send_keys("laptop")
    self.driver.find_element(By.CSS_SELECTOR, ".search-box-button").click()
    self.driver.find_element(By.CSS_SELECTOR, ".product-item img").click()
    self.driver.find_element(By.ID, "add-to-cart-button-31").click()
    self.driver.find_element(By.CSS_SELECTOR, ".content").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ico-cart > .cart-label").click()
    self.driver.find_element(By.ID, "CountryId").click()
    dropdown = self.driver.find_element(By.ID, "CountryId")
    dropdown.find_element(By.XPATH, "//option[. = 'Colombia']").click()
    self.driver.find_element(By.ID, "checkout").click()
    self.driver.find_element(By.CSS_SELECTOR, "p").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ui-button-icon-primary").click()
    self.driver.find_element(By.LINK_TEXT, "Log out").click()
    self.driver.close()
  

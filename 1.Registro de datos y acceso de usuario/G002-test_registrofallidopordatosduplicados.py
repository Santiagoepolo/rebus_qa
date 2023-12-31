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

class TestRegistrofallidopordatosduplicados():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_registrofallidopordatosduplicados(self):
    self.driver.get("https://demowebshop.tricentis.com/")
    self.driver.set_window_size(1366, 728)
    self.driver.find_element(By.LINK_TEXT, "Register").click()
    self.driver.find_element(By.ID, "gender-male").click()
    self.driver.find_element(By.ID, "FirstName").click()
    self.driver.find_element(By.ID, "FirstName").send_keys("Santiago")
    self.driver.find_element(By.ID, "LastName").click()
    self.driver.find_element(By.ID, "LastName").send_keys("Polo")
    self.driver.find_element(By.ID, "Email").click()
    self.driver.find_element(By.ID, "Email").send_keys("Santiago40@hotmail.com")
    self.driver.find_element(By.ID, "Password").click()
    self.driver.find_element(By.ID, "Password").send_keys("qwertyuiop")
    self.driver.find_element(By.ID, "ConfirmPassword").click()
    self.driver.find_element(By.ID, "ConfirmPassword").send_keys("qwertyuiop")
    self.driver.find_element(By.ID, "register-button").click()
    self.driver.find_element(By.CSS_SELECTOR, ".validation-summary-errors li").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".validation-summary-errors li").text == "The specified email already exists"
    self.driver.close()
  

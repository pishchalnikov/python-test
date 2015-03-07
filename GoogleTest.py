from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest, time, re

class GoogleTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.driver.get("http://www.google.com/")
		
	def test_SearchTest(self):
		self.driver.find_element_by_id("lst-ib").clear()
		self.driver.find_element_by_id("lst-ib").send_keys("google search test")
		self.driver.find_element_by_name("btnG").click()
		assert "test" in self.driver.find_element_by_xpath("//*[@id='rso']/div[2]/li[1]").text
	
	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()
	

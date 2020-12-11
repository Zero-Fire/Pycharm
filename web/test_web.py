# -*- coding: utf-8 -*-
import selenium
from selenium import webdriver
import pytest
from selenium.webdriver import ActionChains
from time import sleep

# def test_get():
#     driver = webdriver.Firefox()
#     driver.get("https://ceshiren.com/c/10-category/81-category/81")

class Test_a:
    def setup(self):
        self.driver =webdriver
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()
    @pytest.mark.skip
    def test_a(self):
        self.driver.get("https://testerhome.com/")

        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_link_text("求职面试圈").click()


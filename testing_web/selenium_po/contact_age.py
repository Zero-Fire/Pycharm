# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from testing_web.selenium_po.add_member_page import AddMember
from testing_web.selenium_po.basepage import BasePage


class ContactPage(BasePage):
    def click_add_member(self):
        # opt = webdriver.ChromeOptions()
        # opt.debugger_address="127.0.0.1:9222"
        # self.driver=webdriver.Chrome(options=opt)
        # self.driver.implicitly_wait(5)
        while True:
            self.driver.find_element_by_css_selector(".ww_operationBar .js_add_member").click()
            ele = self.driver.find_elements_by_id("username")
            if len(ele)>0:
                break
        return AddMember(self.driver)
    def get_member(self):
        # opt = webdriver.ChromeOptions()
        # opt.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=opt)
        # self.driver.implicitly_wait(5)
        time.sleep(2)
        eles = self.finds(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
        name_list =[]
        for value in eles:
            name_list.append(value.get_attribute("title"))
        return name_list



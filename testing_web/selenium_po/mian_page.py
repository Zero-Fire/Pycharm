# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from testing_web.selenium_po.basepage import BasePage
from testing_web.selenium_po.contact_age import ContactPage
from testing_web.selenium_po.add_member_page import AddMember


class MainPage(BasePage):

    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def click_contact(self):
        # opt = webdriver.ChromeOptions()
        # opt.debugger_address="127.0.0.1:9222"
        # self.driver = webdriver.Chrome(chrome_options=opt)
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # self.driver.implicitly_wait(5)
        self.find(By.ID,"menu_contacts").click()
        return ContactPage(self.driver)
    def click_add_member_1(self):
        self.find(By.ID, "menu_index").click()
        while True:
            self.find(By.CSS_SELECTOR, "#_hmt_click > div.index_colLeft > div.index_service > div.index_service_cnt."
                                       "js_service_list > a:nth-child(1) > div > span.ww_indexImg.ww_indexImg_AddMember").click()
            element_1 = self.finds(By.ID, "username")
            if len(element_1) > 0:
                break
        return AddMember(self.driver)

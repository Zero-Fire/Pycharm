# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from testing_web.selenium_po.basepage import BasePage
class AddMember(BasePage):
    _name_1= (By.ID,"username")
    _id_1 = (By.ID,"memberAdd_acctid")
    _mail_1=(By.ID,"memberAdd_mail")
    _save_1=(By.CSS_SELECTOR,".ww_operationBar .js_btn_save")
    def add_member(self,name,id,mail):
        from testing_web.selenium_po.contact_age import ContactPage
        # opt = webdriver.ChromeOptions()
        # opt.debugger_address="127.0.0.1:9222"
        # self.driver=webdriver.Chrome(options=opt)
        # self.driver.implicitly_wait(5)
        self.find(*self._name_1).send_keys(name)
        self.find(*self._id_1).send_keys(id)
        self.find(*self._mail_1).send_keys(mail)
        self.find(*self._save_1).click()
        return ContactPage(self.driver)
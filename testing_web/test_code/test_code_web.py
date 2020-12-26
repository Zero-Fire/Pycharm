# -*- coding: utf-8 -*-
import pytest
import yaml
from selenium import webdriver

from testing_web.selenium_po.mian_page import MainPage
with open ("member_data.yaml",encoding="utf-8") as f:
    datas=yaml.safe_load(f)['add']
    data= datas['datas']
class TestCode:

    def setup(self):
        self.main_page = MainPage()
    def teardown(self):
        pass
    @pytest.mark.parametrize("name,id,mail",data)
    def test_code(self,name,id,mail):
        namelist=self.main_page.click_contact().click_add_member().add_member(name,id,mail).get_member()
        assert name in namelist
    @pytest.mark.parametrize("name,id,mail",data)
    def test_code_1(self,name,id,mail):
        namelist = self.main_page.click_add_member_1().add_member(name, id, mail).get_member()
        assert name in namelist

    def test_delete_member(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address="127.0.0.1:9222"
        self.driver=webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_css_selector(".member_colRight_memberTable_th_Checkbox").click()
        self.driver.find_element_by_css_selector(".ww_operationBar .js_delete").click()
        self.driver.find_element_by_css_selector(".ww_dialog_foot .ww_btn_Blue").click()





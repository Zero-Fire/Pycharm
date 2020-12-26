# -*- coding: utf-8 -*-
import time
import pytest
import yaml
from selenium import webdriver
with open("member_data.yaml", encoding="utf-8") as f:
    datas=yaml.safe_load(f)['add']
    data=datas['datas']
    key = datas['keys']
    print(data)
    print(key)
@pytest.mark.parametrize("name,id,mail",data,ids=key)
def test_web(name,id,mail):
    opt = webdriver.ChromeOptions()
    opt.debugger_address="127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(5)
    driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
    driver.find_element_by_id("menu_contacts").click()
    while True:
        driver.find_element_by_css_selector(".ww_operationBar .js_add_member").click()
        element = driver.find_elements_by_id("username")
        if len(element)>0:
            break
    driver.find_element_by_id("username").send_keys(name)
    driver.find_element_by_id("memberAdd_acctid").send_keys(id)
    driver.find_element_by_id("memberAdd_mail").send_keys(mail)
    driver.find_element_by_css_selector(".ww_operationBar .js_btn_save").click()
    time.sleep(3)
    eles = driver.find_elements_by_css_selector(".member_colRight_memberTable_td:nth-child(2)")
    name_list=[]
    for value in eles:
        name_list.append(value.get_attribute("title"))
    assert name in name_list
def test_delete():
    opt = webdriver.ChromeOptions()
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(5)
    time.sleep(1)
    driver.find_element_by_css_selector(".member_colRight_memberTable_th_Checkbox").click()
    time.sleep(1)
    driver.find_element_by_css_selector(".ww_operationBar .js_delete").click()
    time.sleep(1)
    driver.find_element_by_css_selector(".qui_dialog_foot .ww_btn_Blue").click()
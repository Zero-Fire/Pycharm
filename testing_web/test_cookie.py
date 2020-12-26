# -*- coding: utf-8 -*-
import time

import yaml
from selenium import webdriver


def test_get_cookie():
    opt = webdriver.ChromeOptions()
    opt.debugger_address="127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(5)
    cookie = driver.get_cookies()
    # driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    with open ('data_cookie.yaml', "w", encoding="utf-8") as f:
        yaml.dump(cookie,f)
def test_demo():
    opt = webdriver.ChromeOptions()
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="js_contacts46"]/div/div[2]/div/div[2]/div[3]/div[1]/a[1]').click()
    # driver.find_element_by_css_selector("#username").send_keys("张三")
    # driver.find_element_by_css_selector("#memberAdd_acctid").send_keys("111")
    # driver.find_element_by_css_selector('#memberAdd_phone').send_keys('12345678909')
    # driver.find_element_by_xpath('//*[@id="js_contacts46"]/div/div[2]/div/div[4]/div/form/div[3]/a[2]').click()
def test_longin():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
    with open ('data_cookie.yaml',encoding="utf-8") as f:
        yaml_datas = yaml.safe_load(f)
    for cookie in yaml_datas:
        driver.add_cookie(cookie)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    # driver.find_element_by_css_selector("#menu_contacts > span").click()
    # driver.find_element_by_xpath('//*[@id="js_contacts52"]/div/div[2]/div/div[2]/div[3]/div[9]/a[1]').click()
    driver.find_element_by_css_selector('#_hmt_click > div.index_colLeft > div.index_service > div.index_service_cnt.js_service_list > a:nth-child(1) > div > span.ww_indexImg.ww_indexImg_AddMember').click()
    driver.find_element_by_css_selector("#username").send_keys("张三")
    driver.find_element_by_css_selector("#memberAdd_acctid").send_keys("111")
    driver.find_element_by_css_selector('#memberAdd_phone').send_keys('12345678909')
    driver.find_element_by_link_text("保存").click()
    time.sleep(3)
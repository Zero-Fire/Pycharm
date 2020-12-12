# -*- coding: utf-8 -*-
from selenium import webdriver
from time import  sleep
class TestForm:
    def setup(self):
        # self.driver=webdriver.Firefox()
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    def teardown(self):
        pass
        # self.driver.quit()
#简单的自动登陆
    def test_form(self):
        self.driver.get("https://ceshiren.com/")
        self.driver.find_element_by_xpath('/html/body/section/div/div[1]/header/div/div/div[2]/span/button[2]/span').click()
        sleep(1.5)
        self.driver.find_element_by_id("login-account-name").send_keys("992106950@qq.com")
        sleep(1.5)
        self.driver.find_element_by_id("login-account-password").send_keys("628818LY")
        sleep(1.5)
        self.driver.find_element_by_css_selector("#login-button > span:nth-child(2)").click()
        sleep(3)
#QQ邮箱自动登陆，有frame嵌套，要先切换frame，才能查找元素
    def test_form1(self):
        self.driver.get("https://mail.qq.com/")
        sleep(1)
        self.driver.find_element_by_css_selector("#qqLoginTab").click()
        self.driver.switch_to.frame("login_frame")
        self.driver.find_element_by_css_selector('#u').send_keys("1065127019@qq.com")
        sleep(1.5)
        self.driver.find_element_by_id("p").send_keys("13896373854ly")
        sleep(1.5)
        self.driver.find_element_by_css_selector("#login_button").click()
        sleep(3)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        sleep(3)
        self.driver.find_element_by_css_selector("#folder_1").click()
        sleep(3)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_css_selector("a.toptitle:nth-child(7)").click()



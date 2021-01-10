# -*- coding: utf-8 -*-
import time

import pytest
from appium import webdriver


class TestDM:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['noRest'] = 'true'
        desired_caps['dontStopAppOnRest'] = 'true'
        #设置中文输入
        desired_caps['unicodeKeyBoard']='true'
        desired_caps['restKeyBoard']='true'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)
    def teardown(self):
        self.driver.quit()
    def test_demo(self):
        print("这是一个测试用例")
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        time.sleep(3)
        self.driver.back()

    if __name__ == '__main__':
        pytest.main

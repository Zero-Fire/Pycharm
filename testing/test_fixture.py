# -*- coding: utf-8 -*-
import pytest
#创建登陆的fixture方法;装饰器
@pytest.fixture()  #autosue 自动使用 不需要调用
def login():
    print("执行登陆操作") # setup操作
    username="123"
    password="123"
    token = "1232456"
    yield  [ username,password,token ] #关键字 yield
    # print("登出操作")  # teardown操作，第一次调用是yield之前的内容，第二次调用的yield之后的内容

def test_1(login):
    print(f"longin information:{login}")  #获取返回值，打印返回值
    print("测试用例1")
def test_2(connectDB):
    print("测试用例2")
def test_3(connectDB):
    print("测试用例3")
#或者 两种方法
@pytest.mark.usefixtures("login")
def test_4():
    print("测试用例4")

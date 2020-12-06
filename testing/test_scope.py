# -*- coding: utf-8 -*-
import pytest
# @pytest.fixture(scope='module') #class module session function级别
# def connectDB():
#     print('链接数据库')
#     yield
#     print("断开数据库")
class TestDemo:
    def test_a(self,connectDB):
        print("这是测试用例a")
    def test_b(self,connectDB):
        print("这是测试用例b")
class TestDemo1:
    def test_a(self,connectDB):
        print("这是测试用例a")
    def test_b(self,connectDB):
        print("这是测试用例b")
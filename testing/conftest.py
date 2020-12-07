# -*- coding: utf-8 -*-
import yaml
import pytest
import os
from Calcu.calc_code import Calculator
from typing import List
# @pytest.fixture(scope='session') #class module function 级别
# def connectDB():
#     print('链接数据库')
#     yield
#     print("断开数据库")
@pytest.fixture(scope="module")
def get_calc():
    calc=Calculator()
    return calc
#设置yaml文件的绝对路径
yaml_file_path = os.path.dirname(__file__) + "/data/calc_data.yaml"
# with open ('./data/calc_data.yaml',encoding='utf-8') as f:
with open (yaml_file_path,encoding='utf-8') as f:
    add_data=yaml.safe_load(f)['add']
    data=add_data['data']
    key=add_data['key']
    div=add_data['div']
    keys=add_data['keys']
    sub_data=add_data['sub_data']
    sub_key=add_data['sub_key']
    mul_data=add_data['mul_data']
    mul_key=add_data['mul_key']
@pytest.fixture(params=data,ids=key)
def get_add_data(request):
    print("开始计算")
    datas=request.param
    yield datas
    print("结束计算")
@pytest.fixture(params=div,ids=keys)
def get_div_data(request):
    data=request.param
    print("开始计算")
    yield data
    print("结束计算")
@pytest.fixture(params=sub_data,ids=sub_key)
def get_sub_data(request):
    data = request.param
    print("开始计算")
    yield data
    print("计算结束")
@pytest.fixture(params=mul_data,ids=mul_key)
def get_mul_data(request):
    data=request.param
    print("开始计算")
    yield data
    print("结束计算")
def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    # 实现用例反转执行
    # items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')



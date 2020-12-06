# -*- coding: utf-8 -*-
import pytest
@pytest.fixture(params=[1,2,3])
def login1(request):
    data=request.param
    print("获取测试数据")
    return data+1

def test_a(login1):
    print(login1)
    print("111")

# -*- coding: utf-8 -*-
import yaml
import pytest
from Calcu.calc_code import Calculator


def setup_module():
    print('计算开始')

def teardown_module():
    print('计算结束')

with open ('./data/calc_data.yaml',encoding='utf-8') as f:
    add_data=yaml.safe_load(f)['add']
    data=add_data['data']
    key=add_data['key']
    div=add_data['div']
    keys=add_data['keys']
    sub_data=add_data['sub_data']
    sub_key=add_data['sub_key']
    mul_data=add_data['mul_data']
    mul_key=add_data['mul_key']

class TestCalculator:


    @pytest.mark.parametrize(
        'a,b,expect', data,
        ids=key
    )
    def test_add(self,a,b,expect):
        #实例化计算器类
        calc = Calculator()
        result=calc.add(a,b)
        #判断结果是否为浮点类型，是就保留2位小数
        if isinstance(result,float):
            result=round(result,2)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect',div,ids=keys)

    def test_div(self,a,b,expect):
        calc = Calculator()
        result = calc.div (a,b)
        if isinstance(result,float):
            result=round(result,2)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect',sub_data,ids=sub_key)

    def test_sub(self,a,b,expect):
        calc = Calculator()
        result=calc.sub(a,b)
        if isinstance(result,float):
            result=round(result,4)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect',mul_data,ids=mul_key)
    def test_mul(self,a,b,expect):
        calc=Calculator()
        result = calc.mul(a,b)
        if isinstance(result,float):
            result = round(result,4)
        assert result == expect



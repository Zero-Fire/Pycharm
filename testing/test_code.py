# -*- coding: utf-8 -*-
import yaml
import pytest
from Calcu.calc_code import Calculator


def setup_module():
    print('计算开始')

def teardown_module():
    print('计算结束')

with open ('./data/calc_data.yaml') as f:
    add_data=yaml.safe_load(f)['add']
    data=add_data['data']
    key=add_data['key']
    div=add_data['div']
    keys=add_data['keys']


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

class TestCalculator_1:

    @pytest.mark.parametrize('a,b,expect',div,ids=keys)

    def test_div(self,a,b,expect):
        calc = Calculator()
        result = calc.div (a,b)
        if isinstance(result,float):
            result=round(result,2)
        assert result == expect



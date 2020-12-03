# -*- coding: utf-8 -*-
import yaml
import pytest
from Calcu.calc_code import Calculator
with open ('./data/calc_data.yaml') as f:
    add_data=yaml.safe_load(f)['add']
    data=add_data['data']

class TestCalculator:

    @pytest.mark.parametrize(
        'a,b,expect',data,
        ids=['int']
    )
    def setup_class(self):
        print('计算开始')

    def teardown_class(self):
        print('计算结束')

    def test_add(self,a,b,expect):
        #实例化计算器类
        calc= Calculator()
        result=calc.add(a,b)
        #判断结果是否为浮点类型，是就保留2位小数
        if isinstance(result,float):
            result=round(result,2)
        assert result == expect



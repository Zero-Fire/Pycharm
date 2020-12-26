# -*- coding: utf-8 -*-
import pytest
import allure


# def setup_module():
#     print('计算开始')
#
# def teardown_module():
#     print('计算结束')

# with open ('./data/calc_data.yaml',encoding='utf-8') as f:
#     add_data=yaml.safe_load(f)['add']
#     data=add_data['data']
#     key=add_data['key']
#     div=add_data['div']
#     keys=add_data['keys']
#     sub_data=add_data['sub_data']
#     sub_key=add_data['sub_key']
#     mul_data=add_data['mul_data']
#     mul_key=add_data['mul_key']
# @pytest.fixture(scope="module")
# def get_calc():
#     calc=Calculator()
#     return calc

# @pytest.fixture(params=data,ids=key)
# def get_add_data(request):
#     print("开始计算")
#     datas=request.param
#     yield datas
#     print("结束计算")

@allure.feature("测试计算器")
class TestCalculator:


    # @pytest.mark.parametrize(
    #     'a,b,expect', data,
    #     ids=key
    # )
    @allure.story("测试加法")
    @pytest.mark.run(order=1)
    @pytest.mark.add
    def test_add(self,get_add_data,get_calc):
        #实例化计算器类
        # calc = Calculator()
        result = None
        try:
            with allure.step("计算两个数的相加值"):
                result=get_calc.add(get_add_data[0],get_add_data[1])
        #判断结果是否为浮点类型，是就保留2位小数
            if isinstance(result,float):
                result=round(result,2)
        except Exception as e:
            print(e)
        assert result == get_add_data[2]

    # @pytest.mark.parametrize('a,b,expect',div,ids=keys)
    #
    @allure.story("测试除法")
    @pytest.mark.div
    @pytest.mark.last
    def test_div(self,get_div_data,get_calc):
        # calc = Calculator()
        result = None
        try:
            with allure.step("计算两个数的相除值"):
                result = get_calc.div (get_div_data[0],get_div_data[1])
            if isinstance(result,float):
                result=round(result,2)
        except Exception as e:
            print(e)
        assert result == get_div_data[2]
    #
    # @pytest.mark.parametrize('a,b,expect',sub_data,ids=sub_key)
    #
    @allure.story("测试减法")
    @pytest.mark.sub
    @pytest.mark.run(order=2)
    def test_sub(self,get_calc,get_sub_data):
        # calc = Calculator()
        result = None
        try:
            with allure.step("计算两个数的相减值"):
                result=get_calc.sub(get_sub_data[0],get_sub_data[1])
            if isinstance(result,float):
                result=round(result,4)
        except Exception as e:
            print(e)
        assert result == get_sub_data[2]
    #
    # @pytest.mark.parametrize('a,b,expect',mul_data,ids=mul_key)
    @pytest.mark.mul
    @allure.story("测试乘法")
    @pytest.mark.run(order=3)
    def test_mul(self,get_calc,get_mul_data):
        # calc=Calculator()
        result = None
        try:
            with allure.step("计算两个数的相乘值"):
                result = get_calc.mul(get_mul_data[0],get_mul_data[1])
            if isinstance(result,float):
                result = round(result,4)
        except Exception as e:
            print(e)
        assert result == get_mul_data[2]



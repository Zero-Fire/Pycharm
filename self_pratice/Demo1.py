# -*- coding: utf-8 -*-
#字典
# dict_a={"a":1,"b":2}
# dict_b=dict(a=1,b=2)
# b=dict_a.fromkeys((1,2,3),"a")
# print(b)
# print({i: i * 2 for i in range(1, 4)})
# print(dict_a.keys())
# print(dict_a.values())
# print(dict_b.pop("a"))
# print(dict_a)
# print(dict_b)



# #集合 a=set(1,2,3)
# a={1,2,3}
# b={1,4,5}
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# a.add('a')
# print(a)
# print({i for i in "werweffwwerfdfewr"})
# #去重
# c='dfsdfewfwef'
# print(set(c))

# a=[1,2,3] #元祖 a = (1,2,3) 不可变数据类型
# print(a)
# b=(1,2,a,1)
# b[2][0]="a"
# print(b)
# print(b.index(a))


#列表推导式
# a=[]
# for i in range(1,4):
#     a.append(i**2)
# print(a)
# b=[i**2 for i in range(1,4)]
# print(b)
# c=[i*j*k for i in range(1,4) for j in range(4,9) for k in range(2,5)]
# print(c)
# d=[i**2 for i in range(1,5) if i==1]
# print(d)


# def fun1(a=1,b=1,c=1):
#     print("这是一个函数")
#     return a,b,c
# #看返回值需要打印出来,调用函数时，没有传递参数则使用默认参数
# # print(fun1(2,3,4))
# print(fun1())
# fun2=lambda x,y: y+x*2
# #= def fun3(x):
#  #   return x*2
# print(fun2(2,1))
def mul (a,b):
    try:
        if isinstance(a,(int,float)) and isinstance(b,(int,float)):
            return a*b
        else:
            return "请输入数字"
    except Exception as e:
        print(e)

print(mul(1,','))
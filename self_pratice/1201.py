# -*- coding: utf-8 -*-
class person:
    name : str = None
    age : int = 0
    gen : str = "男"
    __money : float = 20000
    def __init__(self,name,age,gen,money):
        print('这是一个构造函数')
        self.name = name
        self.age = age
        self.gen=gen
        self.__money=money
    def get_money(self):
        return self.__money
    def eat (self):
        print(f"{self.name} is eating")
        return  True

    def run(self):
        print('run')

    def jump(self):
        print(f"{self.name} is jumping")

class funnyman(person):
    skill : str = ''

    def __init__(self,skill,name,age,gen,money):
        self.skill=skill
        super().__init__(name,age,gen,money)
    def fun(self):
        print(f'{self.name} is funny')

st = funnyman('haha','st',20,'男',2000)
print(st.name)
st.fun()

# zs=person('张三',20,'男',2000)
# print(zs.name)
# print(zs.age)
# print(zs.gen)
# zs.eat()
# print(zs.get_money())
# # print(dir(zs))
# zs.jump()
# zs.name='王五'
# person.name="default"
# print(person.name)
# print(zs.name)
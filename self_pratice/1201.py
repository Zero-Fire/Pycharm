# -*- coding: utf-8 -*-
class person:
    name : str = None
    age : int = 0
    gen : str = "男"
    __money : float = 20000
    def __init__(self,name,age,gen,money):
        self.name = name
        self.age = age
        self.gen=gen
        self.__money=money
    def eat (self):
        print(f"{self.name} is eating")
        return  True

    def run(self):
        print('run')

    def jump(self):
        print(f"{self.name} is jumping")
zs=person('张三',20,'男',2000)
print(zs.name)
zs.eat()
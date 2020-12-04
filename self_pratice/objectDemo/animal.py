# -*- coding: utf-8 -*-
import yaml
class Animal:
    name:str = None
    age:int = None
    color :str = None
    gender :str = None
    def __init__(self,name,age,color,gender):
        self.name = name
        self.age = age
        self.color = color
        self.gender = gender
    def run(self):
        print(f'{self,name},会跑')

    def call(self):
        print(f'{self.name}会叫')

class Cat(Animal):

    def __init__(self,hair,name,age,color,gender):
        self.hair = hair
        super().__init__(name,age,color,gender)

    def skill(self):
        print(f'{self.name}会抓老鼠,它的名字叫{self.name}，它年龄是{self.age}，他的毛发是{self.color}，它的性别是{self.gender}')

    def call(self):
        print(f'{self.name}会喵喵叫')

class Dog(Animal):

    def __init__(self,hair,name,age,color,gender):
        self.hair= hair
        super().__init__(name,age,color,gender)

    def call(self):
        print(f'{self.name}会汪汪叫')

    def skill(self):
        print(f'{self.name}会看家,它的名字是{self.name}，它的年龄是{self.age}，他的颜色是{self.color}，他的性别是{self.gender}')
# Tom=Cat("短发",'Tom',2,'黑色','male')
# dog=Dog("长发",'旺财',4,'黄色','female')


if __name__=='__main__':
    with open('data_animal.yaml', encoding='utf-8') as f:
        data1 = yaml.safe_load(f)['data']
        data = data1['Cat']
        name = data['name']
        age = data['age']
        color = data['color']
        hair = data['hair']
        gender = data['gender']
    Tom = Cat(hair,name,age,color,gender)
    Tom.skill()
    Tom.call()
    data = data1['Dog']
    name = data['name']
    age = data['age']
    color = data['color']
    hair = data['hair']
    gender = data['gender']
    dog = Dog(hair,name,age,color,gender)
    dog.skill()
    dog.call()



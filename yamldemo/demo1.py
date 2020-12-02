# -*- coding: utf-8 -*-
import  yaml
#定义字典类型 yaml格式
dict = """
    a: 1
    b:
        c: 3
        d: 4
"""
print(yaml.safe_load(dict))
d=yaml.safe_load(dict)
print(type(d))

list=("""
- a
- b
- c
- d
""")
print(yaml.safe_load(list))
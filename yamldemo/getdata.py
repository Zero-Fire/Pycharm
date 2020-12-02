# -*- coding: utf-8 -*-
#yaml.sale_load() 将yaml数据流 转成python对象
#yaml.sale_dump() 将python对象转成yaml数据格式
import yaml

def get_datas():
    with open ('data.yaml',encoding='utf-8') as f:
        datas=yaml.safe_load(f)
    return datas

print(get_datas())

yamlstr=yaml.safe_dump({'languages': ['Ruby', 'Perl', 'Python'], 'websites': {'YAML': 'yaml.org', 'Ruby': 'ruby-lang.org', 'Python': 'python.org'}})
print(yamlstr)

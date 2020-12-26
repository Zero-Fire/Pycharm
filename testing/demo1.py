# -*- coding: utf-8 -*-
import yaml

with open ('./data/calc_data.yaml',encoding='utf-8') as f:
    add_data=yaml.safe_load(f)['add']
    print(add_data)
# -*- coding: utf-8 -*-
import  yaml
class bicycle:
    def run(self, km):
        print(f"健康环保骑行里程数为{km}km")


class EBicycle(bicycle):
    def __init__(self, battery_level):
        self.battery_level = battery_level

    def fill_charge(self, vol):
        self.battery_level = self.battery_level + vol
        # super().__init__(km)

    def run(self, km):
        miles = km - self.battery_level * 10
        if miles > 0:
            print(f'已经使用电行驶{self.battery_level * 10}km')
            Bicycle = bicycle()
            Bicycle.run(miles)
            # 使用super调用
            # super().run(miles)
        else:
            print(f'{km}')


if __name__ == '__main__':
    with open ('bicycle_config.yml') as f:
        datas=yaml.safe_load(f)
    print(datas['e1_level'])
    battery_level=datas['default']['battery_level']
    run_km=datas['default']['run_km']
    eb = EBicycle(battery_level)# 是例子化
    eb.run(run_km)
    # eb = EBicycle(10)
    # eb.run(103)

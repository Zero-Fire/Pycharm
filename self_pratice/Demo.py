# -*- coding: utf-8 -*-
import random
count=0
cpu=random.randint(0,15)
while count<4:
    person = int(input("请输入数字\n"))
    count=count+1
    if person>cpu:
        print("大了")
    elif person==cpu:
        print("对了")
        break
    elif person<cpu:
        print("小了")
if count==4:
    print("真遗憾，机会用完了")
    print("你共猜了：",count,"次")
else:
    print("真棒，你共猜了：", count, "次")



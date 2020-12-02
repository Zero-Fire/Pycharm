# -*- coding: utf-8 -*-
def game():
    my_hp=1000
    my_power=200
    enemy_hp=900
    enemy_power=199
    while True:

        my_hp=my_hp-enemy_power
        enemy_hp=enemy_hp-my_power
    #三目表达式
    # print('i win') if my_final_hp>enemy_final_hp else print('i loss')
        print(my_hp)
        print(enemy_hp)
        if my_hp <= 0:
            print('i loss')
            break
        if enemy_hp<=0:
            print("i win")
            break

game()
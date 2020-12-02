# -*- coding: utf-8 -*-
class Game:
    my_hp = 1000
    my_power = 200
    enemy_hp = 900
    enemy_power = 199

    def __init__(self, my_hp, enemy_hp):
        self.my_hp = my_hp
        self.enemy_hp = enemy_hp

    def fight(self):
        while True:
            self.my_hp = self.my_hp + self.defense - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power
            # 三目表达式
            # print('i win') if my_final_hp>enemy_final_hp else print('i loss')
            print(self.my_hp)
            print(self.enemy_hp)
            if self.my_hp <= 0:
                print('i loss')
                break
            if self.enemy_hp <= 0:
                print("i win")
                break
    def back_home(self):
        print('回城')

class hoyi(Game):
    def __init__(self, defense, my_hp, enemy_hp):
        self.defense = defense
        super().__init__(my_hp, enemy_hp)


#
# game=Game(800,230)
# game.fight()
H = hoyi(200, 1000, 1500)
H.fight()
H.back_home()

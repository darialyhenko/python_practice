from Weapon import Weapon
import random


class Bow(Weapon):

    def __init__(self, name, damage, chance):
        Weapon.__init__(self, name, damage)
        self.__chance = chance

    def bowdamage(self):
        return self.__damage * (self.__chance * 0.01)

    def attack(self):
        chance_attack = self.__chance * 0.01
        rn = random.random()
        if rn <= chance_attack:
            return self.__damage
        else:
            return 0

    def __str__(self):
        return f"Оружие - {self.name}, наносимый урон - {self.damage}, шанс попадания - {self.__chance}"

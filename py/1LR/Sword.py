from Weapon import Weapon
import random

class Sword(Weapon):

    def __init__(self, name, damage, stamina=1):
        Weapon.__init__(self, name, damage)
        self.stamina = stamina

    def attack(self):
        attack_damage = self.damage * self.stamina
        if random.choice([True, False]) == True:
            self.stamina -= 0.1
        return attack_damage

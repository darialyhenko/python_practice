class Warrior:
    def __init__(self, name, strength, health):
        self.name = name
        self.strength = strength
        self.health = health

    def __str__(self):
        return f"{self.name}-й воин, сила атаки - {self.strength}, осталось здоровья - {self.health} HP"

    def __del__(self):
        print('%s-й воин отправляется в Вальгаллу' % self.name)

    def setWeapon(self,weapon):
        self.weapon = weapon

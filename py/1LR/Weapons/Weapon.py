from Effects.Effects import Effects


class Weapon(Effects):
    def __init__(self, name, damage):
        self.name = name
        self.__damage = damage

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, damage):
        if damage > 0:
            self.__damage = damage
        else:
            print("Недопустимый урон")

    def __str__(self):
        return f"Оружие - {self.name}, наносимый урон - {self.damage},{self.effects_print()}"

    def __le__(self, weapon2):
        return self.damage <= weapon2.damage

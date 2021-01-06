class Weapon:
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
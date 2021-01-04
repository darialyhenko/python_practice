class Warrior:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def hit(self):
        self.health = self.health - 20
        return self.health
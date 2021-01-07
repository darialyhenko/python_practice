from abc import ABC


class Effects(ABC):

    @property
    def burn(self):
        return self.burn

    @burn.setter
    def burn(self, count):
        self.burn = count

    def burn_attack(self, warrior):
        if self.burn == 1:
            print('%s-й воин только что был подожжен!' % warrior.name)
            return warrior.health * 0.05
        else:
            return 0

    @property
    def freeze(self):
        return self.freeze

    @freeze.setter
    def freeze(self, count):
        self.freeze = count

    def freeze_attack(self, count):
        if self.freeze == 1:
            return count
        else:
            return 0

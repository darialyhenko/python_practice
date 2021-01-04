from Warrior import Warrior
import random

if __name__ == "__main__":
    unit1 = Warrior('1', 100)
    unit2 = Warrior('2', 100)
    unit3 = Warrior('3', 100)
    unit_list = [unit1, unit2, unit3]

    while True:
        if len(unit_list) == 1:
            print(unit_list[0].name + '-й воин победил')
            break
        x = random.choice(unit_list)
        y = random.choice(unit_list)
        if x != y:
            print('%s-й воин бьет %s-го воина' % (y.name, x.name))
            print('У %s-го воина осталось %s HP \n' % (x.name, x.hit()))
            if x.health <= 0:
                print('%s-й воин погиб от рук %s-го воина\n' % (x.name, y.name))
                unit_list.remove(x)

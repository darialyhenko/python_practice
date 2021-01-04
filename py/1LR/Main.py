from Warrior import Warrior
import random
import copy

if __name__ == "__main__":
    unit1 = Warrior('1', 10, 100)
    unit2 = Warrior('2', 20, 100)
    unit3 = Warrior('3', 50, 100)
    unit_list = [unit1, unit2, unit3]
    copy_unit_list = []

    while True:
        x = random.choice(unit_list)
        y = random.choice(unit_list)
        if x != y:
            print('%s-й воин бьет %s-го воина' % (x.name, y.name))
            y.health -= x.strength
            print('У %s-го воина осталось %s HP \n' % (y.name, y.health))
            copy_unit_list = copy.copy(unit_list)
            for i in range(len(copy_unit_list)):
                if (copy_unit_list[i].health <= 0):
                    unit_list[i].__del__()
                    unit_list.pop(i)
            if len(unit_list) == 1:
                print('Победил %s' % str(unit_list[0]))
                break


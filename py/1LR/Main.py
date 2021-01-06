from Warrior import Warrior
from Bow import Bow
from Sword import Sword

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
                print('\nПобедил %s' % str(unit_list[0]))
                break

    bow1 = Bow("Лук1", random.randint(1, 99), random.randint(1, 99))
    bow2 = Bow("Лук2", random.randint(1, 99), random.randint(1, 99))
    bow3 = Bow("Лук3", random.randint(1, 99), random.randint(1, 99))

    sword1 = Sword("Меч1", random.randint(1, 99), 1)
    sword2 = Sword("Меч2", random.randint(1, 99), 1)
    sword3 = Sword("Меч3", random.randint(1, 99), 1)

    list_weapons = [bow1, bow2, bow3, sword1, sword2, sword3]
    thebest = 0
    print('\nИмеющийся ассортимент оружия:')
    for i in range(len(list_weapons)):
        print(list_weapons[i].__str__())
        if (list_weapons[thebest].__le__(list_weapons[i])):
            thebest = i
    print('\nЛучшее оружие для воина - %s' % (list_weapons[thebest].__str__()))

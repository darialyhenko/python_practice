from Warrior import Warrior
from Weapons.Bow import Bow
from Weapons.Sword import Sword
from Armor import Armor

import random
import copy

if __name__ == "__main__":

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
        if random.choice([True, False]) == True:
            list_weapons[i].freeze()
        if random.choice([True, False]) == True:
            list_weapons[i].burn()
        print(list_weapons[i].__str__())
        if (list_weapons[thebest].__le__(list_weapons[i])):
            thebest = i
    print('\nЛучшее оружие для воина - %s' % (list_weapons[thebest].__str__()))

    armor1 = Armor("Броня1", random.randint(1, 99), 100)
    armor2 = Armor("Броня2", random.randint(1, 99), 100)
    armor3 = Armor("Броня3", random.randint(1, 99), 100)
    armor_list = [armor1,armor2,armor3]
    for i in range(len(armor_list)):
        if random.choice([True, False]) == True:
            armor_list[i].freeze()
        if random.choice([True, False]) == True:
            armor_list[i].burn()

    unit1 = Warrior('1', 3, 100)
    unit2 = Warrior('2', 5, 100)
    unit3 = Warrior('3', 7, 100)
    unit_list = [unit1, unit2, unit3]
    copy_unit_list = []

    weapons_number = random.randint(1, 3)
    for i in range(len(unit_list)):
        random.shuffle(list_weapons)
        unit_list[i].setWeapon(list_weapons[:weapons_number])
        unit_list[i].setArmor(random.choice(armor_list))

    print('\nВоины разобрали свои оружия, битва началась!!!\n')
    while True:
        while True:
            x = random.choice(unit_list)
            if x.weapon[0].stopfight_count == 0:
                break
            print('На %s-его воина действует заморозка еще %s ход(а), он не может никого бить! ' % (x.name, x.weapon[0].stopfight_count))
        y = random.choice(unit_list)
        if x != y and x.weapon[0].stopfight_count == 0:
            print('%s-й воин бьется с %s-м воином' % (x.name, y.name))
            if not x.weapon:
                print('У %s-его воина не осталось оружия! В бой идут кулаки...' % x.name)
                y.health -= x.strength
                print('Мощные кулаки %s-его воина нанесли %s урона!' % (x.name, x.strength))
            else:
                print('Оружие, которое сейчас наносит урон: %s' % x.weapon[0].name)
                print('%s-й воин одет в броню: %s' % (y.name,y.armor.__str__()))
                y.health -= x.weapon[0].burn_attack(y)
                x.weapon[0].freeze_attack(y)
                if type(x.weapon[0]) == Sword and x.weapon[0].stamina == 0:
                    print('У %s-го воина сточился меч! Придется обойтись без него...' % x.name)
                    x.weapon.pop(0)
            print('У %s-го воина осталось %s HP \n' % (y.name, y.health))

            copy_unit_list = copy.copy(unit_list)
            for i in range(len(copy_unit_list)):
                if (copy_unit_list[i].health <= 0):
                    weapon_of_dead = unit_list[i].weapon
                    print('%s-й воин получает все оружие %s-го воина, а именно:' % (x.name, y.name))
                    for j in range(len(weapon_of_dead)):
                        x.weapon.append(weapon_of_dead[j])
                        print('%s' % weapon_of_dead[j].__str__())
                    unit_list[i].__del__()
                    unit_list.pop(i)

            if len(unit_list) == 1:
                print('\nПобедил %s' % str(unit_list[0]))
                break

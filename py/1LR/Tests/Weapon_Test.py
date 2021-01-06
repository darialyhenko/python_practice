import unittest
from Weapon import Weapon


class TestWeaponMethods(unittest.TestCase):

    def test_damage(self):
        weapon = Weapon("Оружие", 50)
        self.assertEqual(weapon.damage, 50)

    def test_damage_setter(self):
        weapon = Weapon("Оружие", 50)
        self.assertEqual(weapon.damage, 50)
        weapon.damage = -20
        self.assertEqual(weapon.damage, 50)
        weapon.damage = 30
        self.assertEqual(weapon.damage, 30)

    def test_le1(self):
        weapon1 = Weapon("Оружие1", 20)
        weapon2 = Weapon("Оружие2", 10)
        self.assertFalse(weapon1.__le__(weapon2))

    def test_le2(self):
        weapon1 = Weapon("Оружие1", 20)
        weapon2 = Weapon("Оружие2", 10)
        self.assertTrue(weapon2.__le__(weapon1))


if __name__ == '__main__':
    unittest.main()

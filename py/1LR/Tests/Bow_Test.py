import unittest
from Weapons.Bow import Bow


class TestBowMethods(unittest.TestCase):

    def test_bowdamage(self):
        bow = Bow("Лук", 50, 100)
        self.assertEqual(bow.damage, 50)

    def test_attack(self):
        bow = Bow("Лук", 50, 100)
        self.assertEqual(bow.damage, 50)

    def test_le1(self):
        bow1 = Bow("Лук1", 50, 100)
        bow2 = Bow("Лук2", 10, 10)
        self.assertFalse(bow1.__le__(bow2))

    def test_le2(self):
        bow1 = Bow("Лук1", 50, 100)
        bow2 = Bow("Лук2", 10, 10)
        self.assertTrue(bow2.__le__(bow1))


if __name__ == '__main__':
    unittest.main()


import unittest
from src.drink import Drink

class DrinkTest(unittest.TestCase):

    def setUp(self):
        self.latte = Drink("Latte", 5, 20)

    def test_drink_has_name(self):
        self.assertEqual("Latte", self.latte.name)

    def test_drink_has_price(self):
        self.assertEqual(5, self.latte.price)

    def test_drink_has_caffeine(self):
        self.assertEqual(20, self.latte.caffeine_level)
    


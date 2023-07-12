# A `Drink` should have a `name`, and a `price`

import unittest
from src.drink import Drink

class DrinkTest(unittest.TestCase):

    def setUp(self):
        self.latte = Drink("Latte", 5)

    def test_drink_has_name(self):
        self.assertEqual("Latte", self.latte.name)

    def test_drink_has_price(self):
        self.assertEqual(5, self.latte.price)


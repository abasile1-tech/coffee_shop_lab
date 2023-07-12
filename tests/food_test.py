import unittest
from src.food import Food

class FoodTest(unittest.TestCase):

    def setUp(self):
        self.sandwich = Food("Sandwich", 7, 30)

    def test_food_has_name(self):
        self.assertEqual("Sandwich", self.sandwich.name)

    def test_food_has_price(self):
        self.assertEqual(7, self.sandwich.price)

    def test_food_has_digestion_level(self):
        self.assertEqual(30, self.sandwich.digestion_level)
    


import unittest
from src.customer import Customer
from src.drink import Drink
from src.food import Food
class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer_1 = Customer("Robert", 100, 50, 30)
        self.latte = Drink("Latter", 5, 20)
        self.sandwich = Food("Sandwich", 7, 30)

    def test_customer_has_a_name(self):
        self.assertEqual("Robert", self.customer_1.name)

    def test_customer_has_a_wallet(self):
        self.assertEqual(100, self.customer_1.wallet)

    def test_spend_money(self):
        self.customer_1.spend_money(5)
        self.assertEqual(95, self.customer_1.wallet)

    def test_buy_a_drink(self):
        self.customer_1.buy_a_drink(self.latte)
        self.assertEqual(95, self.customer_1.wallet)

    def test_buy_food(self):
        self.customer_1.buy_food(self.sandwich)
        self.assertEqual(20,self.customer_1.caffeine_level)
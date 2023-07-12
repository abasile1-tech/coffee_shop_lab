#  - Most coffee shops won't serve coffee to anyone under 16. Add an `age` to the `Customer`. Make sure the `CoffeeShop` checks the `age` before serving the `Customer`.

# add `energy` level to the `Customer`. Every time a `Customer` buys a drink, the `energy` level should go up by the `caffeine_level`.

import unittest
from src.customer import Customer
from src.drink import Drink
class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer_1 = Customer("Robert", 100, 50)
        self.latte = Drink("Latter", 5, 20)

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

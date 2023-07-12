# A `Customer` should have a `name`, and a `wallet`
#   - A `Customer` should have method which reduces the `wallet` by a specified `amount` as a parameter
#   - A `Customer` should be able to buy a `Drink` and reduce their `wallet` by the `Drink`'s price.

import unittest
from src.customer import Customer
from src.drink import Drink
class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer_1 = Customer("Robert", 100)
        self.latte = Drink("Latter", 5)

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

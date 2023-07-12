import unittest
from src.coffee_shop import CoffeeShop
from src.drink import Drink
from src.customer import Customer
class TestCoffeeShop(unittest.TestCase):

#  A `CoffeeShop` should be able to sell a drink to a customer and increase it's `till` by the price of `Drink`. **Hint:** Use a `Customer` method you already have.

# CoffeeShop` should refuse service to a `Customer` with an `energy` above a certain amount!

    def setUp(self):
        self.latte = Drink("latte", 5, 20)
        self.americano = Drink("americano", 4, 30)
        self.drinks = [self.latte, self.americano]
        self.coffee_shop = CoffeeShop("The Prancing Pony", 100, self.drinks)
        self.customer_1 = Customer("Robert", 100, 101)
        self.customer_2 = Customer("Brain", 200, 0)
    
    def test_coffee_shop_has_name(self):
        self.assertEqual("The Prancing Pony", self.coffee_shop.name)

    def test_coffee_shop_has_till(self):
        self.assertEqual(100, self.coffee_shop.till)

    def test_increase_till(self):
        self.coffee_shop.change_till_by_amount(10)
        self.assertEqual(110, self.coffee_shop.till)
    def test_decrease_till(self):
        self.coffee_shop.change_till_by_amount(-10)
        self.assertEqual(90, self.coffee_shop.till)

    def test_has_drink_collection(self):
        self.assertEqual(self.drinks, self.coffee_shop.drinks)

    def test_sell_drink(self):
        self.coffee_shop.sell_drink(self.customer_2, self.latte)
        self.assertEqual(105, self.coffee_shop.till)

    def test_refuse_service(self):
        self.assertEqual(False, self.coffee_shop.sell_drink(self.customer_1, self.latte))
        
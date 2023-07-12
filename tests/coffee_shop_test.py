import unittest
from src.coffee_shop import CoffeeShop
from src.drink import Drink
from src.customer import Customer
class TestCoffeeShop(unittest.TestCase):

    def setUp(self):
        self.latte = Drink("latte", 5, 20)
        self.americano = Drink("americano", 4, 30)
        self.drinks = [self.latte, self.americano]
        self.coffee_shop = CoffeeShop("The Prancing Pony", 100, self.drinks)
        self.customer_1 = Customer("Robert", 100, 101, 30)
        self.customer_2 = Customer("Brain", 200, 0, 30)
        self.customer_3 = Customer("Batman", 4, 10, 30)
        self.customer_4 = Customer("Child",10,0,9)
    
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

    def test_drink_names(self):
        self.assertEqual(["latte", "americano"], self.coffee_shop.drink_names())

    def test_drink_customer_can_afford(self):
        self.assertEqual([self.americano.name], self.coffee_shop.drinks_customer_can_afford(self.customer_3))

    def test_add_to_stock(self):
        self.coffee_shop.add_to_stock(self.latte,5)
        self.assertEqual(5,self.coffee_shop.stock[self.latte])
    
    def test_remove_from_stock(self):
        self.coffee_shop.add_to_stock(self.latte,5)
        self.coffee_shop.remove_from_stock(self.latte, 3)
        self.assertEqual(2,self.coffee_shop.stock[self.latte])

    def test_stock_value(self):
        self.coffee_shop.add_to_stock(self.latte,5)
        self.coffee_shop.remove_from_stock(self.latte, 3)
        self.coffee_shop.add_to_stock(self.americano,11)
        self.assertEqual(13, self.coffee_shop.get_stock_value())

    def test_age_refusal(self):
        self.assertEqual(False, self.coffee_shop.sell_drink(self.customer_4, self.latte))
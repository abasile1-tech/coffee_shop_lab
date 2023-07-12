class CoffeeShop:
    
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks
        self.stock = {}
        for drink in self.drinks:
            self.stock[drink] = 0
            
    def change_till_by_amount(self, amount):
        self.till += amount 

    def sell_drink(self, customer, drink):
        if customer.caffeine_level > 100 or customer.age < 16:
            return False
        else:
            self.change_till_by_amount(drink.price)
            customer.buy_a_drink(drink)
            return True
    
    def drink_names(self):
        return [drink.name for drink in self.drinks]
    
    def drinks_customer_can_afford(self, customer):
        return [drink.name for drink in self.drinks if drink.price <= customer.wallet]

    def add_to_stock(self, drink_to_add, quantity_to_add):
        self.stock[drink_to_add] += quantity_to_add

    def remove_from_stock(self, drink_to_remove, quantity_to_remove):
        while self.stock[drink_to_remove] >= 0 and quantity_to_remove > 0:
            self.stock[drink_to_remove] -= 1
            quantity_to_remove -= 1

    def get_stock_value(self):
        stock_value = 0
        for value in self.stock.values():
            stock_value += value
        return stock_value
        
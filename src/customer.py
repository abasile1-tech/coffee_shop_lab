class Customer:

    def __init__(self, name, wallet, caffeine_level, age):
        self.name = name
        self.wallet = wallet
        self.caffeine_level = caffeine_level
        self.age = age

    def spend_money(self, amount):
        self.wallet -= amount

    def buy_a_drink(self, drink):
        self.spend_money(drink.price)

    def buy_food(self, food):
        self.caffeine_level -= food.digestion_level
        
class Customer:

    def __init__(self, name, wallet, caffeine_level):
        self.name = name
        self.wallet = wallet
        self.caffeine_level = caffeine_level

    def spend_money(self, amount):
        self.wallet -= amount

    def buy_a_drink(self, drink):
        self.spend_money(drink.price)
        
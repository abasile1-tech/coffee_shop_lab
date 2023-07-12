class CoffeeShop:
	
	def __init__(self, name, till, drinks):
		self.name = name
		self.till = till
		self.drinks = drinks
	def change_till_by_amount(self, amount):
		self.till += amount 

	def sell_drink(self, customer, drink):
		if customer.caffeine_level > 100:
			return False
		else:
			self.change_till_by_amount(drink.price)
			customer.buy_a_drink(drink)
			return True
	
	def drink_names(self):
		return [drink.name for drink in self.drinks]
	
	def drinks_customer_can_afford(self, customer):
		return [drink.name for drink in self.drinks if drink.price <= customer.wallet]
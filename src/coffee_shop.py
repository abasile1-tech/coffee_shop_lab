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
		list_of_drinks = []
		for drink in self.drinks:
			list_of_drinks.append(drink.name)
		return list_of_drinks
	
	def drinks_customer_can_afford(self, customer):
		drinks_customer_can_afford = []
		for drink in self.drinks:
			if drink.price <= customer.wallet:
				drinks_customer_can_afford.append(drink.name)
		return drinks_customer_can_afford
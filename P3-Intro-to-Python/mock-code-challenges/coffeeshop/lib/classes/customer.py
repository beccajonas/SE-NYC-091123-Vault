class Customer:    
    def __init__(self, name):
        self.name = name
        self.transactions = []
        self.coffees = []

    def __repr__(self):
        return f"Customer: {self.name}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str) or len(name) < 1 or len(name) > 15:
            raise Exception ("Name must be string between 1-15 characters")
        self._name = name

    def access_current_transactions(self, new_transaction=None):
        from classes.transaction import Transaction
        if isinstance(new_transaction, Transaction):
            self.transactions.append(new_transaction)
        return self.transactions

    def access_current_coffees(self, new_coffee=None):
        from classes.coffee import Coffee
        if new_coffee is not None and isinstance(new_coffee, Coffee) and new_coffee not in self.coffees:
            self.coffees.append(new_coffee)
        return self.coffees

    def place_order(self, name_of_coffee, price):
        from classes.coffee import Coffee
        from classes.transaction import Transaction
        return Transaction(self, Coffee(name_of_coffee), price)

    def calculate_total_money_spent(self):
        total_price = 0
        for transaction in self.transactions:
            total_price += transaction.price
        return total_price
    
    def retrieve_coffees_within_price_range(self, min_price=0, max_price=999):
        filtered_coffees = []
        for transaction in self.transactions:
            if min_price <= transaction.price <= max_price:
                filtered_coffees.append(transaction.coffee)
        return filtered_coffees
class Customer:    
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            if len(name) >= 1 and len(name) <= 15:
                self._name = name
        else: raise Exception("Name must be a string between 1-15 characters long")

    def __repr__(self):
        return f"Customer: {self.name}"

    def access_current_transactions(self, new_transaction=None):
        from classes.transaction import Transaction
        pass

    def access_current_coffees(self, new_coffee=None):
        from classes.coffee import Coffee
        pass

    def place_order(self, name_of_coffee, price):
        pass

    def calculate_total_money_spent(self):
        pass
    
    def retrieve_coffees_within_price_range(self, min_price=0, max_price=999):
        pass
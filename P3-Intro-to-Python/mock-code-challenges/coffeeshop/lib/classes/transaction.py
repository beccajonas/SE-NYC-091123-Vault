class Transaction:
    counter, catalog = 0, []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

        Transaction.counter += 1
        Transaction.catalog.append(self)
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if isinstance(price, int):
            if price >= 1 and price <= 50:
                self._price = price
        else: raise Exception("Price must be between 1 and 50")


    def __repr__(self):
        return f"{self.customer.name} ordered a {self.coffee.name} for ${self.price}."
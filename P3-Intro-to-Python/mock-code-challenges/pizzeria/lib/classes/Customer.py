class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []
        self.pizzas = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str) or len(name) > 15 or len(name) < 1:
            raise Exception("Names must be at least 1 character and at most 15 characters long")
        self._name = name

    def access_current_orders(self, new_order=None):
        from classes.Order import Order
        if new_order is not None and isinstance(new_order, Order):
            self.orders.append(new_order)
        return self.orders

    def access_current_pizzas(self, new_pizza=None):
        from classes.Pizza import Pizza
        if new_pizza is not None and isinstance(new_pizza, Pizza) and new_pizza not in self.pizzas:
            self.pizzas.append(new_pizza)
        return self.pizzas
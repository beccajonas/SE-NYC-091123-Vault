class Order:
    def __init__(self, customer, pizza, price):
        self.customer = customer
        self.pizza = pizza
        self.price = price

        pizza.access_current_orders(self)
        pizza.access_current_customers(customer)

        customer.access_current_orders(self)
        customer.access_current_pizzas(pizza)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if price > 10 or price < 1:
            raise Exception("Price must be at least 1 and no greater than 10")
        self._price = price
    
    @property
    def customer(self):
        return self._price
    
    @customer.setter
    def customer(self, customer):
        from classes.Customer import Customer
        if not isinstance(customer, Customer):
            raise Exception("customer must be of type Customer")
        self._customer = customer
    
    @property
    def pizza(self):
        return self._pizza
    
    @pizza.setter
    def pizza(self, pizza):
        from classes.Pizza import Pizza
        if not isinstance(pizza, Pizza):
            raise Exception("pizza must be of type Pizza")
        self._pizza = pizza
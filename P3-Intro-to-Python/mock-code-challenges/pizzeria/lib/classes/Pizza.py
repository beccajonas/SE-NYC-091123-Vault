class Pizza:
    def __init__(self, name):
        self.name = name
        self.orders = []
        self.customers = []
    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if hasattr(self, "name"):
            raise Exception("Cannot change pizza after its been created")
        self._name = name
    
    def access_current_orders(self, new_order=None):
        from classes.Order import Order
        if new_order is not None and isinstance(new_order, Order):
            self.orders.append(new_order)
        return self.orders 
    
    def access_current_customers(self, new_customer=None):
        from classes.Customer import Customer
        if new_customer is not None and isinstance(new_customer, Customer) and new_customer not in self.customers:
            self.customers.append(new_customer)
        return self.customers
    
    def calculate_total_number_of_orders(self):
        return len(self.orders)
    
    def calculate_average_price_across_all_orders(self):
        total = 0
        for pizza in self.orders:
            total += pizza.price
        return total / len(self.orders)
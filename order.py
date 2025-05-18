from customer import Customer
from coffee import Coffee

class Order:
    _all_orders = []
    def __init__(self, customer, coffee, price):
        # self._customer = customer
        # self._coffee = coffee

        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be an instance of Coffee")
        if not isinstance(price, float):
            raise ValueError("Price must be a float.")
        if not isinstance(price, float):
            raise ValueError("Price must be a float.")
        if not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0.")
        self._price = price
        self._customer=customer 
        self._coffee=coffee
        
        Order._all_orders.append(self)

    @property
    def price(self):
        return self._price
    @property
    def customer(self):
        return self._customer
    @property
    def coffee(self):
        return self._coffee
    @classmethod
    def all(cls):
        return cls._all_orders



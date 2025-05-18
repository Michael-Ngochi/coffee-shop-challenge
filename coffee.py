class Coffee:
    def __init__(self,name):
        if not isinstance(name,str):
            print("Name should be a string")
        elif not len(name) >=3:
            print("Name should be at least 3 characters long")
        else:
            self._name=name
    @property
    def name(self):
        return self._name
    @property
    def orders(self):
        from order import Order
        return [order for order in Order.all() if order.coffee == self]
    @property
    def customers(self):
        from order import Order
        return list({order.customer for order in Order.all() if order.coffee == self})
    def num_orders(self):
        from order import Order
        count= sum(1 for order in Order.all() if order.coffee == self)
        return count
    def average_price(self):
        from order import Order
        prices= [order.price for order in Order.all() if order.coffee == self]
        return sum(prices) / len(prices) if prices else 0




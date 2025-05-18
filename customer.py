class Customer:
    def __init__(self,name):
            self._name=name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        if not isinstance(value,str):
            print("Name should be a string")
        elif not 1<= len(value) <=15:
            print("Name should be between 1 to 15 characters")
        else:
            self._name=value
    @property
    def orders(self):
        from order import Order
        return [order for order in Order.all() if order.customer == self]
    @property
    def coffees(self):
        from coffee import Coffee
        return list({order.coffee for order in self.orders})


    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)

        
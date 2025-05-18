from customer import Customer
from coffee import Coffee
print(f"[DEBUG] Running order.py as: {__name__}")

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


espresso = Coffee("Espresso")
latte = Coffee("Latte")
cappuccino = Coffee("Cappuccino")
mocha = Coffee("Mocha")
americano = Coffee("Americano")
macchiato = Coffee("Macchiato")
flat_white = Coffee("Flat White")
cold_brew = Coffee("Cold Brew")


Marry= Customer("Marry")
MyOrd3 = Order(Marry,latte,9.0)
MyOrd4 = Order(Marry,latte,9.0)
MyOrd5 = Order(Marry,cold_brew,3.0)
 
Bob= Customer("Bob")
MyOrd = Order(Bob,mocha,8.0)
MyOrd2 = Order(Bob,flat_white,7.0)
MyOrd6 = Order(Bob,latte,7.0)


# print(MyOrd.customer.name)
# print(MyOrd.coffee.name)
 
 

# for order in Marry.orders:
#     print(order.customer.name)
#     print(order.coffee.name)
#     print(order.price)
    



# for coffee in Marry.coffees:
#     print(coffee.name) 



# for order in latte.orders:
#     print(f"{order.customer.name} ordered a {order.coffee.name}")


# for customer in latte.customers: 
#     print(customer)


# Bob.create_order(macchiato,5.0)
# for coffee in Bob.coffees:
#     print(coffee.name) 
 
# print(latte.num_orders())



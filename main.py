from customer import Customer
from coffee import Coffee
from order import Order

latte = Coffee("Latte")
bob = Customer("Bob")

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


# print(mocha.average_price())


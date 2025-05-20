# Coffee Shop Challenge

This is a simple Python-based system for tracking coffee orders, customers, and coffee types using object-oriented programming principles.

## Project Structure

- `main.py` – The main script used to test the functionality of the classes.
- `coffee.py` – Contains the `Coffee` class that represents a type of coffee.
- `customer.py` – Contains the `Customer` class that represents a customer.
- `order.py` – Contains the `Order` class that links a customer to a coffee order with a price.

## Features

### Customer
- Has a name (1 to 15 characters).
- Can:
  - View their orders.
  - View all coffee types they've ordered.
  - Create new orders.

### Coffee
- Has a name (minimum 3 characters).
- Can:
  - View all orders of that coffee.
  - List all unique customers who ordered it.
  - Count total orders.
  - Calculate average price of the orders.

### Order
- Links a `Customer` and a `Coffee` with a valid price (float between 1.0 and 10.0).
- Maintains a record of all orders made.

## Running the application
1. Run `main.py` to see how it works.

```bash
python main.py
```

> All print statements are commented out by default. Uncomment them to test and explore different features.

## How to Test Functionality

Uncomment the following code blocks in `main.py` to test:

### View orders for a customer
```python
# for order in Marry.orders:
#     print(order.customer.name)
#     print(order.coffee.name)
#     print(order.price)
```

### View all coffee types ordered by a customer
```python
# for coffee in Marry.coffees:
#     print(coffee.name)
```

### View customers who ordered a coffee
```python
# for customer in latte.customers:
#     print(customer.name)
```

### Let a customer place a new order
```python
# Bob.create_order(macchiato, 5.0)
# for coffee in Bob.coffees:
#     print(coffee.name)
```

### Check number of orders for a coffee
```python
# print(latte.num_orders())
```

### Get average price of a coffee
```python
# print(mocha.average_price())
```

## Example Usage

```python
latte = Coffee("Latte")
bob = Customer("Bob")
order = Order(bob, latte, 8.0)

print(order.customer.name)  # Bob
print(order.coffee.name)    # Latte
```

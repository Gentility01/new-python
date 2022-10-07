def products(name, price, quantity):
    output = f"the name of product is {name}:\n price is{price}\n quantity is {quantity}"
    total = price * quantity
    print(output)
    print(f'price of {name} is {total}')

products('charger', 2000, 5)
products('Laptop', 20000, 20)
products('mouse', 10000, 10)

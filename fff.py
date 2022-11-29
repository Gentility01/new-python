# def products(name, price, quantity):
#     output = f"the name of product is {name}:\n price is{price}\n quantity is {quantity}"
#     total = price * quantity
#     print(output)
#     print(f'price of {name} is {total}')

# products('charger', 2000, 5)
# products('Laptop', 20000, 20)
# products('mouse', 10000, 10)


import sqlite3
conn = sqlite3.connect('man.db')
cu = conn.cursor()

many_customers = [('chuks', 26), 
                 ('emy', 23, ),
                 ('ebuka', 24)]
# cu.executemany("INSERT INTO doctors VALUES (?,?)", many_customers )  # ??? are the place holders for ech field
cu.execute("DELETE from doctors WHERE rowid = 2")
print('good')

conn.commit()

conn.close()


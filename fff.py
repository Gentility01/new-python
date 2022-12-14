# def products(name, price, quantity):
#     output = f"the name of product is {name}:\n price is{price}\n quantity is {quantity}"
#     total = price * quantity
#     print(output)
#     print(f'price of {name} is {total}')

# products('charger', 2000, 5)
# products('Laptop', 20000, 20)
# products('mouse', 10000, 10)


# import sqlite3
# conn = sqlite3.connect('man.db')
# cu = conn.cursor()

# many_customers = [('chuks', 26), 
#                  ('emy', 23, ),
#                  ('ebuka', 24)]
# # cu.executemany("INSERT INTO doctors VALUES (?,?)", many_customers )  # ??? are the place holders for ech field
# cu.execute("DELETE from doctors WHERE rowid = 2")
# print('good')

# conn.commit()

# conn.close()

# import numpy as np
# a = np.array([[1,'obinna', 20], [2, 'chidi', 23], [3, 'Onyii', 13]])

# # print(a[1])
# print(a.dtype)


# f = open('items.csv', 'r')
# print(f.mode)
# f.close()

# with open('oop2.html', 'w') as f:
#     f.write('<h1>writing into file</h1>') #this will add what we have in this bracket into the new file that is created
#     f.write('<h2>this is just another line written </h2>') #this will add what we have in this bracket into the new file that is created
#     f.write('<h3>this is just another line written </h3>') #this will add what we have in this bracket into the new file that is created
#     f.write('<h4>this is just another line written </h4>') #this will add what we have in this bracket into the new file that is created
#     f.write('<h1>this is just another line written </h1>') #this will add what we have in this bracket into the new file that is created
#     f.write('<h6>this is just another line written </h6>') #this will add what we have in this bracket into the new file that is created

import sqlite3


with open('man.html', 'w') as f:
    conn = sqlite3.connect('man.db')
    c = conn.cursor()
    result = c.execute("SELECT * FROM doctors")
    f.write(str(result))
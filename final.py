import sqlite3
con = sqlite3.connect('my_customer.db')
c = con.cursor()
# c.execute("""CREATE TABLE customers(  
#          first_name text, 
#          last_name text, 
#          email_address text,
#          phone text
    
    
#  ) """)

# c.execute("INSERT INTO customers VALUES ('Mary', 'Doe', 'mary@gmail.com', '081456789') ")  
# print('command executed successfully...')
# many_customers = [('chuks', 'emeka', 'chuls@gmail.com', '0902233345'), 
#                   ('emy', 'joe', 'joe@gmail.com', '0803245678'),
#                   ('ebuka', 'elvin', 'e@gmail.com', '08012234555')]

# c.executemany("INSERT INTO customers VALUES (?,?,?,?)", many_customers )
# print('command executed successfully...')

c.execute("SELECT * FROM customers")
fetch = c.fetchall()
for f in fetch:
    print(f)
print(fetch)
con.commit() 

con.close()
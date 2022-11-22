import sqlite3
con = sqlite3.connect('bank.db')
cus = con.cursor()
cus.execute(""" CREATE TABLE customers(
    first_name text, 
    last_name text, 
    email_address text,
    phone integer
)""")
print('working')
con.close()
# import sqlite3
# con = sqlite3.connect('bank.db')
# cus = con.cursor()
# cus.execute(""" CREATE TABLE customers(
#     first_name text, 
#     last_name text, 
#     email_address text,
#     phone integer
# )""")
# print('working')
# con.close()



n = int(input('enter a number '))
o = str(n)

if n > 50 and n < 100 or o[0] == '7':
    print(True)
else:
    print(False)

# print((50<=n<=100) or (str(n)[0] == 7))
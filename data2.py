import sqlite3

'''LETS KNOW THE DATA TYPES WE HAVE IN sqlite3
Null  --> means doesnot exist
integers --> means real numbers
REAL --> means numbers with decimal
TEXT  --> means just a Text
BLOB  --> means kind of images mp3file or music file ''' 

'''STEPS IN CREATING A DATA IN THE DATABASE'''
# #STEP ONE:
# # creating a connection 

# # con = sqlite3.connect('customer.db')  #when you run this program like this it is going to create a db file\
    
# #STEP ONE:
# # creating a connection 
# '''creating a table and adding table to the table'''
# conn = sqlite3.connect('customer.db')
# # first we need to create a cursor
# # cursor points what we want to do with our table

# #STEP TWO:
# # creating a cusor 
# c = conn.cursor()



# #STEP THREE:
# # creata a table
# #when we want to create a table we use our cursor (command of what our cosor will do)
# #sqlite3 IS CASE SENSITIVE SO  FOLLOW THE SAME STEP Like UPPERCASE CREATE TABLE and lowercase customer 

# '''using a single quotaion mark can make ur code not to be readable'''

# # c.execute("CREATE TABLE customers(  first_name DATATYPE, last_name DATATYPE, email_address DATATYPE) ")


'''using the three quotation mark here make ur code readale'''

# c.execute("""CREATE TABLE customers(  
#         first_name text, 
#         last_name text, 
#         email_address text
    
    
# ) """)


# #STEP FOUR:
# # COMMIT OUR COMMAND TO THE DATABASE(push what ever we have to the database)

# conn.commit() 

#STEP FIVE:
# # close our  connection (anytime we create a connection we should always close it best practice)
# conn.close()


'''INSERT ONE RECORD TO THE DATABASE'''
conn = sqlite3.connect('customer.db')

c = conn.cursor()

# # EXECUTE OUR cusor
c.execute("INSERT INTO customers VALUES ('Mary', 'Doe', 'mary@gmail.com') ")  #sqlite3 COMMAND TO INSERT TABLE

print('command executed successfully...')
conn.commit() 
conn.close()

'''INSERT MANY  TABLE TO THE DATABASE'''

# conn = sqlite3.connect('customer.db')

# c = conn.cursor()

# many_customers = [('chuks', 'emeka', 'chuls@gmail.com'), 
#                  ('emy', 'joe', 'joe@gmail.com'),
#                  ('ebuka', 'elvin', 'e@gmail.com')]
# # EXECUTE OUR cusor
# c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers )  # ??? are the place holders for ech field

# print('command executed successfully...')
# conn.commit() 
# conn.close()

'''QUERY AND FETCH ALL IN THE DATABASE'''

conn = sqlite3.connect('customer.db')

c = conn.cursor()

'''QUERY THE DATABASE'''
# c.execute("SELECT * FROM customers")
'''Primary ID'''
# c.execute("SELECT rowid, * FROM customers")


'''GET THE DATAS'''
# print(c.fetchone()[1])
# c.fetchmany(3)
# items = c.fetchall()
# for item in items:
#     print(item)
# EXECUTE OUR cusor


'''TO SEARCH AND FETCH USING THE WHERE CLAUSE'''

# c.execute("SELECT  * FROM customers WHERE last_name = 'Doe' ")
# c.execute("SELECT  * FROM customers WHERE email_address LIKE 'c%' ")
# item = c.fetchall()
# print(item)

'''UPDATE RECORD'''
# c.execute("""UPDATE customers SET first_name = 'ezinne'
#           WHERE last_name = 'emeka'
          
#           """)
'''a better way  todo this is to use a roll id'''
# c.execute("""UPDATE customers SET first_name = 'Chisom'
#           WHERE rowid = '5'
          
#           """)

'''DELETE RECORD'''
# c.execute("DELETE from customers WHERE rowid = 6")


'''we need to commit this'''
# conn.commit()

# c.execute("SELECT rowid, * FROM customers")

'''QUERY THE DATABASE ORDER BY'''
#by accending
c.execute("SELECT rowid, * FROM customers ORDER BY rowid")
# #by decending
# c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")  #-rowid
# #by lastname with assending
# c.execute("SELECT rowid, * FROM customers ORDER BY last_name ")  

# #by lastname with decending
# c.execute("SELECT rowid, * FROM customers ORDER BY last_name DESC")  

'''QUERY THE DATABASE ORDER BY AND and OR'''
# c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'D%' AND rowid = 2 ")
# c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'D%' OR rowid = 2 ")

'''LIMITING RESULTS'''
# c.execute("SELECT rowid, * FROM customers  ")


'''CREATING A FUNCTION TO USE IN OUR SIMPLEAPP.PY'''
# c.execute("SELECT rowid, * FROM customers ORDER BY rowid LIMIT 1")

# item = c.fetchall()
# # for i in item:
# #     print(i)

# print(item)

# # print('command executed successfully...')
# '''every database created must end with commit and close'''
# conn.commit() 
# conn.close()

'''CREATING A FUNCTION TO USE IN OUR SIMPLEAPP.PY'''
# query the database and return all records
def show_all():
    
    #connecting to the database
    conn = sqlite3.connect('customer.db')
    
    #creating a cursor
    c = conn.cursor()
    # query the database
    c.execute("SELECT rowid, * FROM customers ")

    item = c.fetchall()
    for i in item:
        print(i)



    # print('command executed successfully...')
    '''every database created must end with commit and close'''
    conn.commit() 
    conn.close()
    
'''ADD A NEW RECORD TO OUR TABLE'''
def add_one(first_name, last_name, email_address):
     #connecting to the database
    # conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    # executing and passing in the  parameters
    c.execute("INSERT INTO customers VALUES (?,?,?)", (first_name, last_name, email_address))
    conn.commit() 
    conn.close()
    
'''ADD A NEW MANY TO OUR TABLE'''
def add_many(list):
    
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))
    
    conn.commit() 
    conn.close()


def maintain():
    ...



# 1:24:45
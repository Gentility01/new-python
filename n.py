# import  sqlite3
# conn  =  sqlite3 . connect ( 'now.db' )
# cursor  =  conn.cursor ()
# #create the salesman table 
# cursor.execute("CREATE TABLE salesman(salesman_id n(5), name char(30), city char(35), commission decimal(7,2));")

# s_id = input('Salesman ID:')
# s_name = input('Name:')
# s_city = input('City:')
# s_commision = input('Commission:')
# cursor.execute("""
# INSERT INTO salesman(salesman_id, name, city, commission)
# VALUES (?,?,?,?)
# """, (s_id, s_name, s_city, s_commision))
# conn.commit ()
# print ( 'Data entered successfully.' )
# conn . close ()
# if (conn):
#   conn.close()
#   print("\nThe SQLite connection is closed.")


import  sqlite3
conn = sqlite3.connect('Users.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE users_info2(first_name char(30), last_name char(30), age n(5), gender char(5)    )")

first_name = input('Enter your First name')
last_name = input('Enter your Last name')
age = input('Enter your age')
gender = input('Enter your gender')
cursor.execute("""
INSERT INTO users_info2(first_name, last_name, age, gender)
VALUES (?,?,?,?)
""", (first_name, last_name, age, gender))


conn.commit ()

conn.close

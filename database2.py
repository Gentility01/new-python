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
from datetime import datetime
now = datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
conn = sqlite3.connect('Users.db')
cursor = conn.cursor()
try:
    cursor.execute("CREATE TABLE users_info2(first_name char(30), last_name char(30), age n(5), gender char(5)    )")
    # cursor.execute("ALTER TABLE users_info2 ADD repeat_password null")
except sqlite3.OperationalError:
    first_name = input('Enter your First name \n'.capitalize())
    last_name = input('Enter your Last name \n'.capitalize())
    age = input('Enter your age \n')
    gender = input('Enter your gender \n'.capitalize())
    password = input('Enter your password \n')
    repeat_password = input('Repeat password \n')
    if password != repeat_password:
        print('missmatched password')
        exit()
    else:
        date = formatted_date
        cursor.execute("""
        INSERT INTO users_info2(first_name, last_name, age, gender, password, repeat_password, date)
        VALUES (?,?,?,?,?,?,?)
        """, (first_name, last_name, age, gender, password, repeat_password, date))
# print(formatted_date)


cursor.execute("SELECT rowid, * FROM users_info2")
get_password = cursor.fetchone()
print(get_password[5])

conn.commit ()

conn.close


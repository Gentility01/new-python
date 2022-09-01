
# '''pickle helps us to store all kind of binary data
   
# '''
# '''
# dump() function to store the object data to the file. pickle. dump() function
# takes 3 arguments. The first argument is the object that you want to store.
# The second argument is the file object you get by opening the desired file in write-binary (wb) mode.
# '''

# import pickle
# data = [{"name":"Douglas"}]

# with open("user.pkl", "wb") as f: #wb stands for write byte or binary
  
#     pickle.dump(data, f)

# #the reason we use pickle is to enable us reload the file in its state we left it

# data_from_pkl = pickle.load(open("user.pkl", "rb")) #rb stands for readbyte or binary
# print(data_from_pkl, type(data_from_pkl))



# CONNECTING PYTHON TO MYSQL DATABASE
'''i will be using mysqliteclient 
so i need to install mysqlclient by typing pip install mysqlclient, and if this doesnt work
we usepip install --only-binary :all mysqlclient:

next open ur server on browser and create an empty database
then import  MYSQLdb as mdb
'''

# import MySQLdb as mdb

# DBNAME="dbtest"   #name of the empty database created in our server
# DBHOST = "localhost"
# DBPASS = ""
# DBUSER = "root"

'''CONNECTING  DATABASE TO  SERVER'''

'''trying to connect to the database and  need to pass the variable created into the parameter accodingly
note wont print database connected if it is not connected very well eg. i do not  passin the correct database created'''
# try:
#     db=mdb.connect(DBHOST, DBUSER, DBPASS, DBNAME)
#     print('databasse connected')

# except mdb.Error as e:
#     print('not connected' + e)

'''CREATING TABLES  AND EMPLOY IT '''

# try:
#     db=mdb.connect(DBHOST, DBUSER, DBPASS, DBNAME)  #CONNECTING TO THE DATABASE
#     cur = db.cursor()    #CREATING CURSOR

#     cur.execute("DROP TABLE IF EXISTS Employee")  #creating tables
#     #creating query
#     sqlquery = """
#     CREATE TABLE Employee(
#         Name CHAR(20) NOT NULL,
#         Email CHAR(20),
#         Age INT
#     )
#     """
#     cur.execute(sqlquery)
#     print('Table created successfully connected')

    

# except mdb.Error as e:
#     print('not connected' + e)




'''PUTTING DATA INTO THE TABLE'''
import MySQLdb as mdb

DBNAME="dbtest"   
DBHOST = "localhost"
DBPASS = ""
DBUSER = "root"

#CONNECTING
db=mdb.connect(DBHOST, DBUSER, DBPASS, DBNAME)

#CREATING CURSOR
cur = db.cursor()    

#CREATING AN INSERT QUERY
insertquery = """
INSERT INTO Employee(Name, Email, Age) VALUES('Douglas','douglas@gmail.com', 20)
"""

# EXECUTE QUERYSET IN A TRY AND EXCEPT AND ALSO COMMIT
try:
    cur.execute(insertquery)
    db.commit()
    print('database well commited')
except:
    print('not ok')

db.close()



#15:40

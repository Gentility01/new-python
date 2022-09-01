'''
connecting dababase with wamp need to install  mysqliteclient by typing pip install mysqlclient
if that didnt work you use pip install --only-binary :all: mysqlclient
then connect to ur server(wampserver) and create a new database  in ur admin
next is to import MySQLdb as db by typing  import MySQLdb as mdb
'''
import MySQLdb as mdb

DBNAME = "dbtest"  #this should be the name of the database you created it is not going to work if it is not the same name on the wamserver
DBHOST = "localhost"
DBPASS = ""
DBUSER = "root"


'''next is connecting our db in a try and catch block'''
try:
    db = mdb.connect(DBHOST, DBUSER, DBPASS, DBNAME)
    print('database connected')
except mdb.Error as e:
    print('database not connected' + e)

# run the program and check  if it is connected successfully

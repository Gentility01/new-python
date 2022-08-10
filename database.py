
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
'''we will be using mysqliteclient 
so we need to install mysqlclient by typing pip install mysqlclient, and if this doesnt work
we usepip install --only-binary :all mysqlclient: 
'''
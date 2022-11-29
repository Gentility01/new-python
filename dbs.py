import sqlite3
conn = sqlite3.connect('today.db')
cu = conn.cursor()

a = [('chuks', 'emeka', 12), 
                 ('emy', 'joe', 45),
                 ('ebuka', 'elvin', 20)]
# cu.execute("INSERT INTO todays_table VALUES ('Douglas', 'Cj', 19) ")
cu.executemany("INSERT INTO todays_table VALUES (?,?,?)", a)
print('committedooooo')

conn.commit()
conn.close()
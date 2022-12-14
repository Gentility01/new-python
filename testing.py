import sqlite3
conn = sqlite3.connect("testing.db")

c = conn.cursor()

c.execute("""ALTER TABLE customers  
        ADD  experience varchar(10) """)

# many_customers = [('chuks', 'emeka', 'chuls@gmail.com'), 
#                  ('emy', 'joe', 'joe@gmail.com'),
#                  ('ebuka', 'elvin', 'e@gmail.com')]
# EXECUTE OUR cusor
# c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers )  # ??? are the place holders for ech field
conn.commit()
conn.close()
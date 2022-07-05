import data2

#add a record
data2.add_one("Osoka","Okeke","okeke@gmail.com")

# add many records
stuff = [
    ("Chidindu", 'Okeke', 'chijioke@gmail.com'),
    ("Amanda", 'Amaka', 'amaka@gmail.com'),
    ("Felishia", "Felix", 'felix@gmail.com')
]
data2.add_many(stuff)

#show records
data2.show_all()
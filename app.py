import database

# add a record to the database
#database.add_one("Kobe","Bryant","kobe@bryant.com")

# delete row 6 using 6 as a string
#database.delete_one('6')

# look up email
database.email_lookup("tiamesfahani@yahoo.com")
# will give us the specfic email we are looking for



#add many records
#stuff = [
	#('Andrew', 'luck', 'andrew@luck.com'),
	#('Tom', 'Brady', 'tombrady.com')
	#]
#database.add_many(stuff) # will add these 2 records to the database

#database.show_all()
# if we run it, it all print our database
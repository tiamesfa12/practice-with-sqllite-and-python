# working with the database and importing it
import sqlite3

# connect to the database
conn = sqlite3.connect('customer.db')

# create a cursor
c = conn.cursor()

# Query the Database and return all records
def show_all():
	# connect to the database
	conn = sqlite3.connect('customer.db')

	# create a cursor
	c = conn.cursor()


	c.execute("SELECT rowid, * FROM customers")
	items = c.fetchall()

	for item in items:
		print(item)

	conn.commit()

	conn.close()

# add a new record to the table
def add_one(first,last,email):
	conn = sqlite3.connect('customer.db')		
	c = conn.cursor()
	c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))

	conn.commit()

	conn.close()

def add_many(list):
	conn = sqlite3.connect('customer.db')		
	c = conn.cursor()
	c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))

	conn.commit()

	conn.close()


# delete record from table
def delete_one(id):
	conn = sqlite3.connect('customer.db')		
	c = conn.cursor()
	c.execute("DELETE from customers WHERE rowid = (?)", id)

	conn.commit()

	conn.close()


#lookup with WHERE
def email_lookup(email):
	conn = sqlite3.connect('customer.db')		
	c = conn.cursor()
	c.execute("SELECT * from customers WHERE email = (?)", (email,))
	items = c.fetchall()

	for item in items:
		print(item)

	conn.commit()

	conn.close()





# everything below this is to explain how to create and work with a database
# update records
#c.execute("""UPDATE customers SET first_name = 'Tim'
			#WHERE rowid = 1


	""")

#conn.commit()

# delete records
#c.execute("DELETE from customers WHERE rowid = 6") # will delete the name from row 6

# Query the database - Order by
#c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC") # DESC means descending and will descend the order
# instead of desc you put last_name and will order by the last name

#Query the database - AND/OR, this allows you to look for more conditions/functions in the database
#c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Es%' AND rowid = 3") # returns the name under row 3
# using or could return more than 1 name
# limiting records
#c.execute("SELECT rowid* FROM customers LIMIT 2") # limit results to 2 rows thar are in the database
# Drop Table
#c.execute("DROP TABLE customers") # deletes the table we had made and saved in the database
#conn.commit()

# Query the database
# c.execute("SELECT * FROM customers WHERE last_name = 'Esfahani'") using the where clause
#c.execute("SELECT rowid* FROM customers")
#c.fetchone()
#c.fetchmany(3)
#items = c.fetchall()

#for item in items:
	print(item)

#print("NAME" + "\t\tEMAIL")
#print("--------" + "\t\t--------")
#for item in items:
	#print(item[0] + " " + item[1] + "\t " + item[2])

# create a table
#many_customers = [
#					('Tim', 'Jackson', 'tim@jackson.com'),
#					('Chris', 'Bosh', 'chris@bosh.com'),
#					('Timothy', 'Brown', 'timothy@brown.com'),
#				]

#c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers) # the ? is basically showing first name, last name, and email

# there are 5 types of datatypes when using sqlite3
# NULL - means does it exist or not
# INTEGER - its a whole number
# REAL - its a number with a decimal
# TEXT 
# BLOB

# we need to commit to the database
#conn.commit()

# close the connection
#conn.close() 
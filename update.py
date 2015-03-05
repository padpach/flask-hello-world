import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()
	
	c.execute("UPDATE population SET population = 100000000 WHERE city = 'San Francisco'")
	
	c.execute("DELETE FROM population WHERE city = 'Boston'")
	
	print "\nNEW DATA:\n"
	
	c.execute("SELECT * FROM population")
	
	rows = c.fetchall()
	
	for r in rows:
		print r[0], r[1], r[2]
	
	
# Importar desde CSV

import csv
import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()
	try:
		employees = csv.reader(open("employees.csv", "rU"))
		c.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")
		c.executemany("INSERT INTO employees(firstname, lastname) values(?, ?)", employees)
	except sqlite3.OperationalError:
		print "oops! Algo anda mal!"
	c.close()
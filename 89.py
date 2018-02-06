#Print out the countries that have an area greather than 2,000,000 in the database.db file
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute('SELECT country FROM countries WHERE area > 2000000;')

rows = c.fetchall()
for row in rows:
    print row[0]

conn.close()

'''
conn = sqlite3.connect("database.db")
cur = conn.cursor()
cur.execute("SELECT country FROM countries WHERE area >= 2000000")
rows = cur.fetchall()
conn.close()

for i in rows:
    print(i[0])
'''

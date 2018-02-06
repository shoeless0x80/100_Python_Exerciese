import sqlite3
import csv

conn = sqlite3.connect("database.db")
cur = conn.cursor()
cur.execute("SELECT country FROM countries WHERE area >= 2000000")
rows = cur.fetchall()
conn.close()

new_file = open('90.csv', 'w')
with new_file:
    writer = csv.writer(new_file)
    writer.writerows(rows)

'''
import pandas

df = pandas.DataFrame.from_records(rows)
df.columns = ["Rank", "Country", "Area", "Population"]
df.to_csv("90a.csv", index=False)
'''

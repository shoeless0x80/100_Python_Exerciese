import sqlite3
import pandas

conn = sqlite3.connect("database.db")
cur = conn.cursor()
df = pandas.read_csv('ten-more-countries.txt')
for index, row in df.iterrows():
    eyedee = row['ID']
    country = row['Country']
    area = row['Area']
    cur.execute("INSERT INTO countries ('id', 'country', 'population') VALUES (?, ?, ?)",(eyedee, country, area))

conn.commit()
conn.close()

'''
data = pandas.read_csv("ten_more_countries.txt")

conn = sqlite3.connect("database.db")
cur = conn.cursor()
for index, row in data.iterrows():
    print(row["Country"], row["Area"])
    cur.execute("INSERT INTO countries VALUES (NULL,?,?,NLL)",(row["Country"], row["Area"]))
conn.commit()
conn.close()
'''

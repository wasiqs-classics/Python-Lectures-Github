import sqlite3

db_connect = sqlite3.connect("chinook.db")
cursor = db_connect.cursor()

print("Connection Established")

# READING DATA

query = "INSERT INTO artists (ArtistId, name) VALUES (279, 'Imran Khan')"

cursor.execute(query)
db_connect.commit()

print("Changes saved in database")

query1 = "SELECT * from artists"
cursor.execute(query1)
rows = cursor.fetchall()

for row in rows:
    print(row)


db_connect.close()
import sqlite3 # library for sqlite

# create and connect to the DB

connection = sqlite3.connect("school.db") # this will try to connect to the db and if it does not exist, it will create
cursor = connection.cursor() # this is to get the database running

print("Database connection is activated successfully")

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS classes (
#     class_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     class_name TEXT NOT NULL,
#     teacher TEXT
# )
# """)


# cursor.execute("""
# CREATE TABLE IF NOT EXISTS students (
#     student_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     age INTEGER,
#     gender TEXT,
#     class_id INTEGER,
#     FOREIGN KEY (class_id) REFERENCES classes (class_id)              
# )
# """)

# connection.commit()

# print("Both tables are successfully created!")

# cursor.execute("INSERT INTO classes (class_name, teacher) VALUES (?, ?)", ("Mathematics", "Sir Ali"))

# class_id = cursor.lastrowid # this will give us the id of the last row



# print("Math teacher added")

# students = [
#     ("Alice", 14, "Female", class_id),
#     ("Bob", 15, "Male", class_id)
# ]

# cursor.executemany("INSERT INTO students (name, age, gender, class_id) VALUES (?, ?, ?, ?)", students)

# connection.commit()
# print("Data inserted successfully!")

# Query to select students along with their class details using JOIN
# query = """
# SELECT s.student_id, s.name, s.age, s.gender, c.class_name, c.teacher
# FROM students s
# JOIN classes c ON s.class_id = c.class_id
# WHERE c.class_name = ?
# """

# cursor.execute(query, ("Mathematics",))
# rows = cursor.fetchall()

# for row in rows:
#     print(row)

# Delete student with a specific student_id
# cursor.execute("DELETE FROM students WHERE student_id = ?", (2,))

# connection.commit()
# print("Student deleted successfully!")


connection.close()
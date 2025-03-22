# CRUD Operations
# Create, Read, Update, Delete

import sqlite3

connection = sqlite3.connect("example.db") #it will create the db if it does not exist

cursor = connection.cursor()

print("Connected to the Database successfully")

query1 = """
CREATE TABLE IF NOT EXISTS classes (
    class_id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_name TEXT NOT NULL,
    class_teacher TEXT)
"""

query2 = """
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name TEXT NOT NULL,
    student_age INTEGER,
    student_gender TEXT,
    class_id INTEGER,
    FOREIGN KEY (class_id) REFERENCES classes (class_id)
)
"""

def create_tables():
    cursor.execute(query1)
    cursor.execute(query2)
    connection.commit()
    print("Tables created successfully")

def insert_class(name, teacher):
    query = f"INSERT INTO classes (class_name, class_teacher) VALUES ('{name}','{teacher}')"
    cursor.execute(query)
    print(f"Class with id = {cursor.lastrowid} inserted successfully.")

# insert_class("Physics", "Sir Ahmed")

def insert_students(student_data):
    query = f"INSERT INTO students (student_name, student_age, student_gender, class_id) VALUES (?,?,?,?)"
    cursor.executemany(query, student_data)
    print("Following records entered successfully")
    for student in student_data:
        print(student)

students = [
    ("Ali", 20, "M", 1),
    ("Sara", 22, "F", 1),
    ("Hamza", 21, "M", 2),
    ("Anum", 23, "F", 1),
    ("Kashif", 25, "M", 2),
    ("Nida", 24, "F", 1),
    ("Talha", 26, "M", 1),
    ("Ayesha", 27, "F", 1),
    ("Asad", 28, "M", 2),
    ("Sana", 29, "F", 1),
    ("Raza", 30, "M", 2),
    ("Zara", 31, "F", 1),
    ("Bilal", 32, "M", 2),
    ("Nimra", 33, "F", 1),
    ("Omer", 34, "M", 1),
    ("Maira", 35, "F", 1)
]

# insert_students(students)

def read_data(choice, sub_choice=None):
    if choice == "classes":
        query = "SELECT * FROM classes"
        cursor.execute(query)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    elif choice == "students":
        if sub_choice == None:
            query = """
            SELECT s.student_id, s.student_name, s.student_age, s.student_gender, c.class_name
            FROM students s
            JOIN classes c ON s.class_id = c.class_id
            """
        else:
            query = f"""
            SELECT s.student_id, s.student_name, s.student_age, s.student_gender, c.class_name
            FROM students s
            JOIN classes c ON s.class_id = c.class_id
            WHERE c.class_name = '{sub_choice}'
            """
        cursor.execute(query)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    else:
        print("Invalid Choice")

# read_data("classes")
# read_data("students", "Maths")

def update_student(student_id,**kwargs):
    for key, value in kwargs.items():
        query = f"UPDATE students SET {key} = {value} WHERE student_id = {student_id}"
        cursor.execute(query)
    print(f"Student with id = {student_id} updated successfully")

# read_data("students")

# update_student(15, student_age=40, class_id=2)

# print("After Update")
# read_data("students")

def delete_last_student(id):
    query = f"DELETE FROM students WHERE student_id = {id}"
    cursor.execute(query)
    print(f"Student with id = {id} deleted successfully")

read_data("students")

delete_last_student(13)

read_data("students")

connection.commit()






connection.close()
![Python Database](https://media.geeksforgeeks.org/wp-content/uploads/20211109175603/PythonDatabaseTutorial.png)

# Python Database + CRUD Operations with SQLite

## 1. Introduction

**SQLite** is a lightweight, file-based relational database that is built into Python (via the `sqlite3` module). It is ideal for small to medium-sized applications and is great for learning SQL and database concepts without the overhead of setting up a separate database server.

**Why SQLite?**
- **Easy to use:** No separate server installation required.
- **Portable:** The entire database is stored in a single file.
- **Great for learning:** Simple SQL syntax and full SQL support.

---

## 2. Setting Up SQLite in Python

### **2.1 Installations and Imports**

SQLite comes bundled with Python, so you don’t need to install it separately. Just import the module:

```python
import sqlite3
```

For beginners, it’s useful to also have a SQLite browser tool like [DB Browser for SQLite](https://sqlitebrowser.org/) to visualize your database.

---

## 3. Configuring the Database

### **3.1 Creating and Connecting to a Database**

You can create and connect to an SQLite database using the `sqlite3.connect()` function. This creates a new file if it does not exist.

```python
# Connect to (or create) the database file 'example.db'
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

print("Database connected successfully!")
```

Remember to close your connection after your operations:
```python
conn.close()
```

---

## 4. Creating Tables and Defining Relationships

### **4.1 Writing SQL Queries to Create Tables**

Suppose we want to create a simple database for a school. We’ll create two tables: `students` and `classes`.  
- **students**: Stores student information.
- **classes**: Stores class information.
- We will establish a relationship by adding a foreign key in the `students` table that references the `classes` table.

### **4.2 Example: Creating Tables**

```python
import sqlite3

# Connect to the database
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Create 'classes' table
cursor.execute("""
CREATE TABLE IF NOT EXISTS classes (
    class_id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_name TEXT NOT NULL,
    teacher TEXT
)
""")

# Create 'students' table with a foreign key to 'classes'
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    class_id INTEGER,
    FOREIGN KEY (class_id) REFERENCES classes (class_id)
)
""")

conn.commit()
print("Tables created successfully!")
conn.close()
```

### **Explanation:**
- **`CREATE TABLE IF NOT EXISTS`**: Creates a table only if it doesn’t already exist.
- **Primary Key:** Unique identifier for each record.
- **Foreign Key:** Establishes a relationship between `students.class_id` and `classes.class_id`.

---

## 5. CRUD Operations (Create, Read, Update, Delete)

### **5.1 CREATE: Inserting Data**

#### **Example: Inserting into `classes` and `students`**

```python
import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Insert a new class
cursor.execute("INSERT INTO classes (class_name, teacher) VALUES (?, ?)", 
               ("Mathematics", "Mr. Smith"))
class_id = cursor.lastrowid  # Get the id of the inserted class

# Insert new students
students = [
    ("Alice", 14, "Female", class_id),
    ("Bob", 15, "Male", class_id)
]
cursor.executemany("INSERT INTO students (name, age, gender, class_id) VALUES (?, ?, ?, ?)", students)

conn.commit()
print("Data inserted successfully!")
conn.close()
```

### **5.2 READ: Querying Data**

#### **Example: Selecting All Students in a Specific Class**

```python
import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Query to select students along with their class details using JOIN
query = """
SELECT s.student_id, s.name, s.age, s.gender, c.class_name, c.teacher
FROM students s
JOIN classes c ON s.class_id = c.class_id
WHERE c.class_name = ?
"""

cursor.execute(query, ("Mathematics",))
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
```

### **5.3 UPDATE: Modifying Data**

#### **Example: Updating a Student's Age**

```python
import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Update student age by student_id
cursor.execute("UPDATE students SET age = ? WHERE student_id = ?", (16, 1))

conn.commit()
print("Student updated successfully!")
conn.close()
```

### **5.4 DELETE: Removing Data**

#### **Example: Deleting a Student**

```python
import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Delete student with a specific student_id
cursor.execute("DELETE FROM students WHERE student_id = ?", (2,))

conn.commit()
print("Student deleted successfully!")
conn.close()
```

---

## 6. Writing SQL Queries (A Beginner’s Guide)

### **Key SQL Keywords:**

- **SELECT:** Retrieve data from one or more tables.
- **FROM:** Specify the table.
- **WHERE:** Filter records.
- **INSERT INTO:** Add new records.
- **UPDATE:** Modify existing records.
- **DELETE:** Remove records.
- **JOIN:** Combine rows from two or more tables based on a related column.

### **Example: Basic SELECT Query**

```sql
SELECT name, age FROM students WHERE gender = 'Female';
```
This query retrieves the names and ages of all female students.

### **Example: Complex Query with JOIN**

```sql
SELECT s.name, s.age, c.class_name 
FROM students s
JOIN classes c ON s.class_id = c.class_id
WHERE s.age > 14;
```
This query selects the names and ages of students older than 14 along with their class names.

---

## 7. Summary

- **Setup:** Use `sqlite3.connect()` to create/connect to an SQLite database.
- **Creating Tables:** Write SQL `CREATE TABLE` queries. Define primary keys and foreign keys for relationships.
- **CRUD Operations:**  
  - **CREATE:** `INSERT INTO`  
  - **READ:** `SELECT` (optionally with `JOIN`, `WHERE`)
  - **UPDATE:** `UPDATE`  
  - **DELETE:** `DELETE FROM`
- **SQL Queries:** Use basic keywords (`SELECT`, `WHERE`, `JOIN`, etc.) to retrieve and manipulate data.

---

## 8. Practice Exercises

1. **Setup Exercise:**  
   Create an SQLite database named `library.db` and create two tables: `authors` (author_id, name, nationality) and `books` (book_id, title, author_id, published_year). Define a foreign key in `books` referencing `authors`.

2. **CRUD Operations:**  
   Insert data into both tables. Write queries to:  
   - List all books along with their authors' names.  
   - Update a book’s published year.  
   - Delete an author and all their books (you might need to use cascading deletes or write a query to delete from books first).

3. **Dynamic Query:**  
   Write a Python function that accepts a nationality and retrieves all authors from that country along with the titles of their books.

4. **Complex Query:**  
   Write a query to count the number of books published after a certain year, grouped by author.

---

## 9. Conclusion

This tutorial provided a detailed guide on setting up an SQLite database, configuring tables with relationships, and performing CRUD operations using SQL queries in Python. With this knowledge, you'll be able to design and implement database-driven applications. Happy coding, and enjoy working with SQLite!

## 10. Further Reading
1. [A short Tutorial on SQL Queries](https://github.com/wasiqs-classics/Python-Lectures-Github/blob/master/Module%203%20-%20Advance%20Topics/019%20Database%20and%20CRUD/SQL_Intro.md)
2. [Geeks for Geeks Python Database Resources](https://www.geeksforgeeks.org/python-database-tutorial/)

[![Prev Lecture](../../Previous.png)](https://github.com/wasiqs-classics/Python-Lectures-Github/tree/master/Module%203%20-%20Advance%20Topics/018%20More%20Advanced%20Topics)       [![Next Lecture](../../Next.png)](https://github.com/wasiqs-classics/Python-Lectures-Github/tree/master/Module%203%20-%20Advance%20Topics/020%20GUI%20Programming)
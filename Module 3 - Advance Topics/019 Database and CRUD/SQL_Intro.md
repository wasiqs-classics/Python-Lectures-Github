# **SQL Querying Basics & Running Queries in SQLite (Short Tutorial)**  

This tutorial will cover:  
1️⃣ **Basics of SQL Queries** (SELECT, INSERT, UPDATE, DELETE)  
2️⃣ **Intermediate & Advanced Queries** (JOIN, GROUP BY, ORDER BY, Subqueries)  
3️⃣ **Executing Queries in SQLite** (Static & Dynamic queries)  

---

## **1️⃣ Basics of SQL Queries**  

SQL (**Structured Query Language**) is used to manage and manipulate databases. The most commonly used SQL commands are:  
🔹 `SELECT` → Retrieve data  
🔹 `INSERT INTO` → Add data  
🔹 `UPDATE` → Modify existing data  
🔹 `DELETE` → Remove data  
🔹 `CREATE TABLE` → Create a new table  
🔹 `ALTER TABLE` → Modify a table structure  
🔹 `DROP TABLE` → Delete a table  

---

### **🔹 SELECT Statement (Retrieving Data)**
Fetches data from a table.

```sql
SELECT * FROM students;
```
➡ Retrieves **all** columns from the `students` table.

```sql
SELECT name, age FROM students;
```
➡ Retrieves **only** the `name` and `age` columns.

```sql
SELECT * FROM students WHERE age > 18;
```
➡ Retrieves students **older than 18**.

---

### **🔹 INSERT INTO (Adding Data)**
Used to add new records.

```sql
INSERT INTO students (name, age, gender) VALUES ('Alice', 22, 'Female');
```
➡ Adds a student named "Alice".

To add multiple records:
```sql
INSERT INTO students (name, age, gender) VALUES
('Bob', 20, 'Male'),
('Charlie', 19, 'Male');
```

---

### **🔹 UPDATE (Modifying Data)**
Modifies existing records.

```sql
UPDATE students SET age = 21 WHERE name = 'Alice';
```
➡ Updates Alice’s age to **21**.

To update multiple fields:
```sql
UPDATE students SET age = 22, gender = 'Female' WHERE name = 'Alice';
```

---

### **🔹 DELETE (Removing Data)**
Deletes records from a table.

```sql
DELETE FROM students WHERE name = 'Bob';
```
➡ Deletes **Bob** from the database.

Delete **all** records (⚠ **Use carefully**!):
```sql
DELETE FROM students;
```

---

## **2️⃣ Intermediate & Advanced Queries**  

### **🔹 ORDER BY (Sorting Results)**
Used to sort query results in ascending or descending order.

```sql
SELECT * FROM students ORDER BY age ASC;
```
➡ Sorts students by age in **ascending order**.

```sql
SELECT * FROM students ORDER BY age DESC;
```
➡ Sorts students by age in **descending order**.

---

### **🔹 GROUP BY (Grouping Data)**
Groups rows that have the same values.

```sql
SELECT gender, COUNT(*) FROM students GROUP BY gender;
```
➡ Counts the number of students grouped by **gender**.

---

### **🔹 JOIN (Combining Data from Multiple Tables)**
Combines rows from two or more tables based on a related column.

#### **Example: Students & Classes**
```sql
SELECT students.name, students.age, classes.class_name
FROM students
JOIN classes ON students.class_id = classes.class_id;
```
➡ Retrieves **student names, ages, and their class names**.

---

### **🔹 Subqueries (Nested Queries)**
A query inside another query.

```sql
SELECT name FROM students WHERE age = (SELECT MAX(age) FROM students);
```
➡ Retrieves the **oldest student**.

---

### **🔹 LIKE (Pattern Matching)**
Used to search for a specific pattern.

```sql
SELECT * FROM students WHERE name LIKE 'A%';
```
➡ Retrieves names that **start with 'A'**.

```sql
SELECT * FROM students WHERE name LIKE '%son';
```
➡ Retrieves names that **end with 'son'**.

---

### **🔹 LIMIT (Restricting Results)**
Limits the number of results returned.

```sql
SELECT * FROM students LIMIT 5;
```
➡ Retrieves **only the first 5** students.

---

## **3️⃣ Executing Queries in SQLite with Python**  

### **🔹 Setting Up SQLite in Python**
```python
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("school.db")
cursor = conn.cursor()
```

---

### **🔹 Executing Static Queries**
Static queries don’t take user input; they execute predefined SQL statements.

#### **Fetching All Students**
```python
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)
```

#### **Inserting a Student**
```python
cursor.execute("INSERT INTO students (name, age, gender) VALUES ('Alice', 22, 'Female')")
conn.commit()
```

#### **Updating a Student**
```python
cursor.execute("UPDATE students SET age = 23 WHERE name = 'Alice'")
conn.commit()
```

#### **Deleting a Student**
```python
cursor.execute("DELETE FROM students WHERE name = 'Alice'")
conn.commit()
```

---

### **🔹 Executing Dynamic Queries (Using User Input)**
Dynamic queries allow user interaction.

#### **Using `?` Placeholders (Safer Method to Prevent SQL Injection)**
```python
name_input = input("Enter the name to search: ")
cursor.execute("SELECT * FROM students WHERE name = ?", (name_input,))
rows = cursor.fetchall()
print(rows)
```

#### **Using Named Placeholders (`:parameter_name`)**
```python
name_input = input("Enter the name to update age: ")
new_age = int(input("Enter new age: "))

cursor.execute("UPDATE students SET age = :new_age WHERE name = :name",
               {"new_age": new_age, "name": name_input})
conn.commit()
```

---

### **🔹 Deleting Based on User Input**
```python
name_input = input("Enter the name to delete: ")
cursor.execute("DELETE FROM students WHERE name = ?", (name_input,))
conn.commit()
print(f"Deleted {name_input} from the database.")
```

---

### **🔹 Executing Queries with Multiple Inputs (Using `executemany()`)**
For inserting multiple records at once:
```python
students = [
    ('Bob', 20, 'Male'),
    ('Charlie', 21, 'Male'),
    ('Daisy', 22, 'Female')
]
cursor.executemany("INSERT INTO students (name, age, gender) VALUES (?, ?, ?)", students)
conn.commit()
```

---

### **🔹 Fetching Query Results Dynamically**
Fetching and displaying records based on input criteria:

#### **Search Students by Age**
```python
age_input = int(input("Enter the age: "))
cursor.execute("SELECT * FROM students WHERE age = ?", (age_input,))
rows = cursor.fetchall()
for row in rows:
    print(row)
```

#### **Displaying Records in a Table Format**
```python
import pandas as pd

cursor.execute("SELECT * FROM students")
df = pd.DataFrame(cursor.fetchall(), columns=['ID', 'Name', 'Age', 'Gender'])
print(df)
```

---

## **4️⃣ Summary of Key Concepts**
| **SQL Command** | **Purpose** | **Example** |
|---------------|------------|------------|
| `SELECT` | Retrieve data | `SELECT * FROM students;` |
| `INSERT INTO` | Add new data | `INSERT INTO students (name, age) VALUES ('Alice', 22);` |
| `UPDATE` | Modify data | `UPDATE students SET age = 23 WHERE name = 'Alice';` |
| `DELETE` | Remove data | `DELETE FROM students WHERE name = 'Alice';` |
| `ORDER BY` | Sort results | `SELECT * FROM students ORDER BY age DESC;` |
| `GROUP BY` | Aggregate results | `SELECT gender, COUNT(*) FROM students GROUP BY gender;` |
| `JOIN` | Combine tables | `SELECT students.name, classes.class_name FROM students JOIN classes ON students.class_id = classes.class_id;` |
| `LIMIT` | Restrict results | `SELECT * FROM students LIMIT 5;` |

---

## **5️⃣ Practice Exercises**
1️⃣ **Create a new table** `teachers (id, name, subject)` and insert records.  
2️⃣ **Write a query** to find students older than **20** who are in **Mathematics class**.  
3️⃣ **Write a Python script** to prompt the user for a name and retrieve their details.  
4️⃣ **Modify a student's age** using a **Python script** with `UPDATE`.  
5️⃣ **Write a DELETE query** to remove all students **younger than 18**.  

---

## **6️⃣ Conclusion**
- SQL is **powerful for managing data** in structured databases.  
- **Static queries** execute pre-defined SQL statements.  
- **Dynamic queries** allow **user input** for filtering, updating, and deleting records.  
- Use **placeholders (`?` or `:name`) to prevent SQL injection.**  
- SQLite + Python is an **easy and efficient** way to manage small to medium-scale applications.  

**🚀 Next Steps:** Try integrating SQLite queries with **Streamlit for a full-fledged web application!**
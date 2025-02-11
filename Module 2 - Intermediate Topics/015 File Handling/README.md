# **Lecture: File Handling in Python**  

---

## **1. Introduction to File Handling**  

File handling is an essential part of programming as it allows us to **store, retrieve, and manipulate data** persistently. Python provides a simple and efficient way to work with files using the built-in `open()` function.  

### **Why Use File Handling?**  
- **Permanent Data Storage**: Files allow data to persist beyond program execution.  
- **Data Logging**: Logs can be stored in files for later analysis.  
- **Data Transfer**: Files facilitate data sharing between different programs or systems.  
- **Working with Large Data**: Storing structured data such as text, CSV, or JSON.  

---

## **2. Opening and Closing Files in Python**  

### **Using `open()` Function**  
```python
file = open("example.txt", "r")  # Opens file in read mode
file.close()  # Always close the file after usage
```
💡 **Why Close Files?**  
- Prevents data corruption.  
- Frees up system resources.  
- Ensures all data is written properly before program exits.  

### **Using `with` Statement (Best Practice)**  
```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # File is automatically closed after this block
```
💡 **Advantages of `with` Statement**:  
- No need to explicitly close the file.  
- Automatically handles exceptions.  

---

## **3. File Access Modes in Python**  

| **Mode** | **Description** |
|----------|---------------|
| `"r"`  | Read mode (default). Opens file for reading. |
| `"w"`  | Write mode. Creates a new file if not exists, overwrites if exists. |
| `"a"`  | Append mode. Adds content at the end of the file without erasing existing data. |
| `"x"`  | Exclusive mode. Creates a new file but raises an error if file exists. |
| `"r+"` | Read and Write mode. Requires the file to exist. |
| `"w+"` | Write and Read mode. Overwrites the file content. |
| `"a+"` | Append and Read mode. |

---

## **4. Reading Files in Python**  

### **Reading the Entire File**
```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```
### **Reading Line by Line**
```python
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # Removes extra spaces and new lines
```
### **Using `readline()`**
```python
with open("example.txt", "r") as file:
    print(file.readline())  # Reads only one line at a time
```
### **Using `readlines()` (Reading into a List)**
```python
with open("example.txt", "r") as file:
    lines = file.readlines()
    print(lines)  # Each line is stored as an item in a list
```

---

## **5. Writing to a File**  

### **Overwriting a File (`w` Mode)**
```python
with open("example.txt", "w") as file:
    file.write("Hello, World!\nThis is a new file.")
```
💡 **Warning**: This mode will **erase existing content** before writing new data.

### **Appending to a File (`a` Mode)**
```python
with open("example.txt", "a") as file:
    file.write("\nThis line is appended.")
```

---

## **6. Updating a File (`r+` and `w+` Modes)**  

### **Modify Specific Lines in a File**
```python
with open("example.txt", "r") as file:
    lines = file.readlines()

# Modify content (Example: Replacing a word)
updated_lines = [line.replace("Hello", "Hi") for line in lines]

with open("example.txt", "w") as file:
    file.writelines(updated_lines)
```

---

## **7. Deleting a File Using `os` Module**  
```python
import os

if os.path.exists("example.txt"):
    os.remove("example.txt")
    print("File deleted successfully.")
else:
    print("File does not exist.")
```
💡 **Warning**: Always **check if a file exists** before deleting to prevent errors.

---

## **8. Working with CSV Files (Without `pandas`)**  

CSV files are widely used to store structured data in **rows and columns**, separated by commas.

### **Writing Data to a CSV File**
```python
import csv

data = [
    ["Name", "Age", "City"],
    ["Alice", "25", "New York"],
    ["Bob", "30", "London"]
]

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
```
💡 **Key Points**:  
- `newline=""` ensures proper formatting.  
- `writerows()` writes multiple rows to the CSV.  

### **Reading a CSV File**
```python
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Each row is a list
```

### **Appending Data to a CSV File**
```python
import csv

new_data = ["Charlie", "35", "Paris"]

with open("data.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(new_data)
```

---

## **9. Practical Examples**

### **Example 1: Logging Events to a File**  
```python
import time

def log_event(event):
    with open("log.txt", "a") as file:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} - {event}\n")

log_event("User logged in.")
log_event("File downloaded.")
```
💡 **Why Use Logging?**  
- Keeps track of important system/user events.  
- Helps in debugging.  

---

### **Example 2: Searching for a Word in a File**  
```python
def search_word(file_name, word):
    with open(file_name, "r") as file:
        lines = file.readlines()
        for index, line in enumerate(lines, start=1):
            if word in line:
                print(f"Found '{word}' in line {index}: {line.strip()}")

search_word("example.txt", "Python")
```
💡 **Use Cases**:  
- Searching for specific logs or errors in a large text file.  

---

### **10. File Handling Best Practices**  
✅ Always close files after use (or use `with`).  
✅ Handle **exceptions** when dealing with file operations.  
✅ Check if a **file exists** before reading or deleting.  
✅ Use **CSV files** for structured tabular data.  
✅ Avoid overwriting files accidentally (use `"a"` mode carefully).  

---

## **11. Conclusion**  

File handling is a fundamental skill in Python that enables **data storage, retrieval, and manipulation**. By mastering file operations, you can effectively work with **logs, text files, and structured CSV data**. The **open() function, file modes, and with statement** are crucial for managing file operations efficiently.  

More details [can be found here](https://github.com/wasiqs-classics/Code-Camp-Python-for-Data-Science-and-Machine-Learning/blob/master/Python%20Lect%2010%20-%20Advance%20Python%20Topics%20-1.pdf)

🚀 **Next Step:** Let's explore a complicated example which covers almost all the topics we went through earlier. 
Click here: 

---
## **12. Practice Exercises**  

1️⃣ **Basic File Handling**:  
   - Create a program that asks the user to enter text and saves it into a file.  

2️⃣ **Read & Modify a File**:  
   - Write a Python script that reads a file and replaces all occurrences of the word `"Python"` with `"Java"`.  

3️⃣ **CSV File Handling**:  
   - Create a CSV file storing student records (name, age, marks).  
   - Write a program to **read the file** and print all student details.  

4️⃣ **Word Count in a File**:  
   - Write a Python script to count how many times a given word appears in a file.  

---



![Cover](https://media.geeksforgeeks.org/wp-content/uploads/20201125211352/PythonJSON.jpg)

# **Lecture 14: Working with JSON in Python**  

---

## **1. Introduction to JSON**  

### **What is JSON?**  
JSON (**JavaScript Object Notation**) is a **lightweight data-interchange format** used to store and transfer data. It is **human-readable, easy to parse, and language-independent**, making it widely used in APIs, databases, and data storage.  

### **Why Use JSON?**  
- **Data Exchange**: JSON is commonly used to send and receive data between a server and a web application.  
- **Configuration Files**: Many software applications use JSON for settings and preferences.  
- **Database Storage**: NoSQL databases like MongoDB store data in JSON format.  
- **Easy Parsing**: JSON is structured and can be parsed easily in most programming languages.  

---

## **2. The `json` Module in Python**  

Python provides a built-in `json` module to work with JSON data. It allows us to **convert Python objects to JSON format** and vice versa.  

### **Importing the JSON Module**  
```python
import json
```

---

## **3. JSON Structure**  

JSON data is written as **key-value pairs** (like a Python dictionary) and can include **arrays, nested objects, strings, numbers, booleans, and null values**.  

### **Example JSON Data**  
```json
{
    "name": "Alice",
    "age": 25,
    "email": "alice@example.com",
    "skills": ["Python", "Machine Learning"],
    "is_student": false
}
```

This JSON object contains:  
- **String values**: `"Alice"`, `"alice@example.com"`  
- **Integer value**: `25`  
- **Boolean value**: `false`  
- **Array/List**: `["Python", "Machine Learning"]`

---

## **4. JSON Parsing (Deserialization) in Python**  

### **Converting JSON String to Python Dictionary**  

```python
import json

json_data = '{"name": "Alice", "age": 25, "email": "alice@example.com"}'

# Converting JSON string to Python dictionary
python_dict = json.loads(json_data)

print(python_dict["name"])  # Output: Alice
print(type(python_dict))    # Output: <class 'dict'>
```
💡 **Explanation**:  
- `json.loads()` is used to **parse** a JSON string into a **Python dictionary**.  

---

## **5. JSON Serialization (Encoding Python Objects to JSON Format)**  

### **Converting a Python Dictionary to JSON String**  
```python
import json

python_dict = {
    "name": "Alice",
    "age": 25,
    "email": "alice@example.com"
}

# Convert Python dictionary to JSON string
json_data = json.dumps(python_dict)

print(json_data)         # Output: JSON formatted string
print(type(json_data))   # Output: <class 'str'>
```
💡 **Explanation**:  
- `json.dumps()` is used to **convert a Python dictionary into a JSON-formatted string**.  

---

## **6. Reading and Writing JSON Files**  

### **Reading JSON from a File**  
```python
import json

# Open and read JSON file
with open("data.json", "r") as file:
    data = json.load(file)

print(data)  # Output: Python dictionary
```
💡 **Explanation**:  
- `json.load()` is used to **read and parse JSON data from a file into a Python dictionary**.  

---

### **Writing JSON to a File**  
```python
import json

data = {
    "name": "Bob",
    "age": 30,
    "city": "New York"
}

# Write dictionary to a JSON file
with open("output.json", "w") as file:
    json.dump(data, file, indent=4)  # Pretty format with 4-space indentation
```
💡 **Explanation**:  
- `json.dump()` is used to **write a Python dictionary into a JSON file**.  

---

## **7. Pretty-Printing JSON**  

### **Formatting JSON for Readability**
```python
import json

data = {
    "name": "Alice",
    "age": 25,
    "email": "alice@example.com",
    "skills": ["Python", "Machine Learning"]
}

json_formatted = json.dumps(data, indent=4, sort_keys=True)
print(json_formatted)
```
💡 **Explanation**:  
- `indent=4` → Makes JSON output **more readable**.  
- `sort_keys=True` → Sorts keys alphabetically.  

---

## **8. Handling Complex Data Types**  

JSON **does not support Python-specific data types** like tuples or datetime objects.  

### **Handling Non-Serializable Data (Custom Encoder)**  
```python
import json
from datetime import datetime

# Custom JSON Encoder for datetime
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()  # Convert datetime to ISO string
        return super().default(obj)

data = {
    "event": "Conference",
    "date": datetime.now()
}

json_data = json.dumps(data, cls=DateTimeEncoder, indent=4)
print(json_data)
```
💡 **Explanation**:  
- Python `datetime` is **not JSON serializable**, so we create a **custom encoder**.  

---

## **9. Error Handling in JSON Parsing**  

### **Handling Invalid JSON**  
```python
import json

invalid_json = "{'name': 'Alice', 'age': 25}"  # Invalid JSON (single quotes)

try:
    data = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print("Error:", e)
```
💡 **Explanation**:  
- JSON must use **double quotes** (`"`) for keys and string values.  

---

## **10. Practical Examples of JSON in Python**  

### **Example 1: Web API Data Parsing (REST API)**  
```python
import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
users = response.json()  # Convert JSON response to Python list

for user in users[:3]:  # Display first 3 users
    print(user["name"], "-", user["email"])
```
💡 **Explanation**:  
- **Web APIs return JSON responses** that can be parsed and used directly.  

---

### **Example 2: Storing User Preferences in a JSON File**  
```python
import json

user_prefs = {
    "theme": "dark",
    "font_size": 14,
    "language": "English"
}

# Save user settings to file
with open("settings.json", "w") as file:
    json.dump(user_prefs, file, indent=4)

# Load user settings from file
with open("settings.json", "r") as file:
    prefs = json.load(file)

print(prefs["theme"])  # Output: dark
```
💡 **Explanation**:  
- JSON is commonly used for **storing configuration settings**.  

---

## **11. Exercises**  

1. **JSON File Handling:**  
   - Write a Python program that reads a JSON file containing a list of products (name, price, stock) and prints details of all available products.  

2. **API JSON Parsing:**  
   - Use `requests` to fetch **random user data** from [https://randomuser.me/api/](https://randomuser.me/api/) and extract the name, email, and country.  

3. **Validating JSON Data:**  
   - Write a program that takes user input in JSON format and checks if it follows the correct structure (must contain `"name"` and `"age"` keys).  

4. **Converting CSV to JSON:**  
   - Read a CSV file and convert it into a JSON file with proper formatting.  

---

## **12. Conclusion**  

JSON is an essential format for data exchange, storage, and API communication. With Python’s built-in `json` module, you can efficiently parse, serialize, read, and write JSON data. Mastering JSON will enable you to work with **REST APIs, databases, web scraping, and data analytics** more effectively.  

---

[![Prev Lecture](../../Previous.png)](https://github.com/wasiqs-classics/Python-Lectures-Github/tree/master/Module%202%20-%20Intermediate%20Topics/013%20RegEx)       [![Next Lecture](../../Next.png)](https://github.com/wasiqs-classics/Python-Lectures-Github/tree/master/Module%202%20-%20Intermediate%20Topics/015%20File%20Handling)
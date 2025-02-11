### **Comprehensive File Handling Example**  

This example demonstrates **functions, JSON, file handling, error handling, modules, and RegEx** while working with **randomized CSV data**.  

---

## **1. Problem Statement**  
We will:  
1. **Generate fake data** using three lists:  
   - **Names** (Pakistani names)  
   - **Locations** (Pakistani cities)  
   - **Products** (Commonly sold products)  
2. **Create a CSV file** containing **50 random entries** from the lists.  
3. **Implement a search function** that filters data by city and returns results in JSON format.  
4. **Create a function to return matched data as a dictionary**.  

---

## **2. Import Required Modules**  
```python
import csv
import json
import random
import os
import re
```
- **`csv`** → To handle CSV file operations.  
- **`json`** → To convert matched data to JSON format.  
- **`random`** → To randomly select names, locations, and products.  
- **`os`** → To handle file operations.  
- **`re`** → To validate city names.  

---

## **3. Step 1: Creating Random Data & Writing to CSV**  

```python
# Lists of random data
list_names = ["Raheel", "Kashif", "Ayesha", "Wasiq", "Sara", "Ahmed", "Hina", "Bilal", "Fatima", "Hassan"]
list_locations = ["Karachi", "Lahore", "Islamabad", "Quetta", "Peshawar", "Faisalabad", "Multan", "Sialkot"]
list_products = ["Shoes", "Mobile", "Clothes", "Furniture", "Laptop", "Marble", "Watch", "Books", "Camera"]

# Function to create a CSV file with random data
def create_csv(filename="data.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Location", "Product"])  # Header row

        for _ in range(50):  # Create 50 random entries
            name = random.choice(list_names)
            location = random.choice(list_locations)
            product = random.choice(list_products)
            writer.writerow([name, location, product])

    print(f"CSV file '{filename}' created successfully!")

# Call function to generate data
create_csv()
```
💡 **Concepts Covered**:  
- **Random selection** from lists.  
- **Writing to CSV file** using `csv.writer()`.  
- **Looping to generate multiple entries**.  

---

## **4. Step 2: Filtering Data by Location & Returning JSON**  

```python
# Function to read CSV and return data based on location
def filter_by_location(location, filename="data.csv"):
    if not os.path.exists(filename):
        print("Error: CSV file not found!")
        return None

    pattern = re.compile(r"^[A-Za-z ]+$")  # Regex to validate location name
    if not pattern.match(location):
        print("Error: Invalid location format!")
        return None

    results = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Location"].lower() == location.lower():
                results.append(row)

    if results:
        json_result = json.dumps(results, indent=4)
        print(f"Data for location '{location}':\n{json_result}")
        return json_result
    else:
        print(f"No records found for location '{location}'.")
        return None

# Example: Get data for "Karachi"
filter_by_location("Karachi")
```
💡 **Concepts Covered**:  
- **Reading CSV file** using `csv.DictReader()`.  
- **Filtering data based on user input**.  
- **Using `re` module for validation** (ensuring the location contains only letters).  
- **Converting results to JSON format** with `json.dumps()`.  
- **Error handling** for file existence and invalid input.  

---

## **5. Step 3: Returning Matched Data as a Dictionary**  

```python
# Function to return all matched data as a dictionary
def get_data_as_dict(location, filename="data.csv"):
    json_data = filter_by_location(location, filename)  # Get JSON results

    if json_data:  # Convert JSON string to Python dictionary
        data_dict = json.loads(json_data)
        return data_dict
    else:
        return None

# Example usage
data_dict = get_data_as_dict("Lahore")

if data_dict:
    print("\nDictionary Format Output:")
    print(data_dict)
```
💡 **Concepts Covered**:  
- **Converting JSON back to a Python dictionary** with `json.loads()`.  
- **Reusing the previous function (`filter_by_location()`)** to avoid redundant code.  
- **Returning structured data for further processing**.  

---

## **6. Summary of Concepts Covered**  

| Concept            | Explanation |
|-------------------|-------------|
| **Functions** | Encapsulating logic into reusable functions. |
| **JSON Handling** | Converting CSV data to JSON format. |
| **File Handling** | Reading and writing CSV files. |
| **Error Handling** | Checking if files exist and handling invalid input. |
| **Regex Validation** | Ensuring only valid location names are entered. |
| **Randomization** | Generating random sample data for realistic scenarios. |
| **Modules** | Using built-in Python modules (`csv`, `json`, `os`, `random`, `re`). |

---

## **7. Practice Exercises**  

1️⃣ **Modify the Program**  
   - Allow the user to **input the number of entries** to generate in the CSV file.  

2️⃣ **Enhance Data Filtering**  
   - Modify `filter_by_location()` to allow **searching by product** instead of location.  

3️⃣ **Export to JSON File**  
   - Instead of printing JSON, write the output to a **separate JSON file**.  

4️⃣ **User Interaction**  
   - Build a simple CLI (Command Line Interface) that asks users for location input and returns results.  

---

## **8. Conclusion**  

This example provided a **practical way to integrate multiple Python concepts** in one project. We:  
✅ Created a **CSV file** with random data.  
✅ Implemented **functions** to filter data dynamically.  
✅ Used **JSON formatting** to make results structured.  
✅ Added **error handling** for invalid inputs and missing files.  
✅ Introduced **Regex validation** for location names.  

🚀 **Next Steps:** Try modifying the functions to make the project more interactive!
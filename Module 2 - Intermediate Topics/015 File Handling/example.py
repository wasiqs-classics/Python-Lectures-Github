import csv
import json
import random
import os
import re

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

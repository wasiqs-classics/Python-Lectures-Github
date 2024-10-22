# Common Types

# String
name = "Wasiq"

# Integer
age = 37

# Float
salary = 2000.00

# Boolean
is_Married = True

print(id(age)) # printing the memory address of variable age
print(id(name)) # printing the memory address of variable name

# Checking for Type of the variable
print(f"The type of the name variable is: {type(name)}")
print(f"The type of the salary variable is: {type(salary)}")

# Type Conversion

salary = int(salary)

# Now checking the type again. 
print(f"The type of the salary variable is: {type(salary)}")

# Constants
PI = 3.14159
GRAVITY = 9.8

# Collectable Data Types

# List
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4.5]

# Dictionary
student = {"name": "Alice", "age": 20, "grade": "A"}

# Tuple
coordinates = (10, 20)

# Set
unique_numbers = {1, 2, 3, 4}

# Type Hints
first_name: str = "Wasiq" # Here we have already declared the type
last_name: str = "Khan"

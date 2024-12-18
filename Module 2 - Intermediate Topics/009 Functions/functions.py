# # Functions

# # Calculator with functions

# num1 = float(input("Enter numb 1: "))
# num2 = float(input("Enter numb 2: "))
# choice = input("What operation you want to perfomr? (+,-,*,/) ")

# # 1. Function Declaration

# def summ(val1,val2):
#     """
#     This function will output the sum of two numbers
#     """
#     return val1 + val2

# def minus(val1,val2):
#     return val1 - val2

# def multiply(val1,val2):
#     return val1 * val2

# def divide(val1,val2):
#     return val1 / val2

# # 2. Function Calling

# if choice == "+":
#     print(summ(num1,num2))
# elif choice == "-":
#     print(minus(num1,num2))
# elif choice == "*":
#     print(multiply(num1,num2))
# elif choice == "/":
#     print(divide(num1,num2))
# else:
#     print("Wrong Choice")

# Example:

# def hello(name):
#     print(f"Hello {name}!")

# hello("Wasiq")

# Parameters in Functions

# Positional Arguments

# def division(n1,n2=1):
#     if n2 == 0:
#         print("Cannot divide by zero")
#     else:
#         return n1 / n2

# print(division(10,2)) # positional arguments
# print(division(n2=5,n1=3)) # named arguments
# print(division(6)) # default argument 

# def calculate_price(item, price, discount=0):
#     """Calculate the price after applying a discount."""
#     final_price = price - (price * discount / 100)
#     return f"The price of {item} after a {discount}% discount is ${final_price:.2f}"

# # Calling with named parameters
# print(calculate_price(item="Laptop", price=1000, discount=10))
# print(calculate_price(price=500, item="Headphones", discount=5))

# def AddAll(*args):
#     result = 0
#     for arg in args:
#         result += arg
#     return result

# print(AddAll(2,3,4))
# print(AddAll(1,5))

# def info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# info(name="Alice", age=25, city="New York")
# info(name="Wasiq",age=37,gender="male",nationality="Pakistani",id="12345")

# return statement - defines the type of the data and its value stored in the function

# total = AddAll(10,12,93)
# print(total)
# print(AddAll(30,40))

# def Welcome(name):
#     print(f"Hello {name}, welcome to party!")

# message = Welcome("Rayan")
# print(message)

# multiple return values

# def stats(numbers):
#     return min(numbers), max(numbers), sum(numbers)

# print(stats([1, 2, 3]))  # Output: (1, 3, 6)
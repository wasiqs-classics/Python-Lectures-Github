# Checking existing modules

# first we have to import the module

# import math  # this imports the complete math module

# from math import sqrt, pi  # this imports only the sqrt function from the math module

# n = int(input("Enter a number: "))
# square_root_n = sqrt(n)

# print(f"The square root of {n} is {square_root_n}")

# print(f"The value of pi is {pi}")

# import math as m

# print(m.factorial(6))

# importing our custom module

import my_modules as mm

print(mm.func2(1987))

name = mm.values["name"]
print(mm.func1(name))

import os

print(f"CWD isL {os.getcwd()}")


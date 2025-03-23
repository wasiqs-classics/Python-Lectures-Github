# values = []
# for i in range(1,10):
#     if i % 2 == 0:
#         values.append(i*5)
# print(values)

# shortcut = [i*5 for i in range(1,10) if i%2 == 0]
# print(shortcut)

# first_names = ['John', 'Jane', 'Corey', 'Travis']
# last_names = ['Smith', 'Doe', 'Jenkins', 'Davis']

# names_with_j = [f"{first} {last}" for first in first_names for last in last_names if "J" in first and "J" in last]
# print(names_with_j)

# # Create a dictionary with numbers as keys and their squares as values
# squares_dict = {x: x ** 2 for x in range(5)}
# print("Squares Dict:", squares_dict)

# ten_random_names = ['Alice', 'Dob', 'Charlie', 'David', 'Eve', 'Ered', 'George', 'Harry', 'Isabel', 'Back']
# dict_of_names = {char : [name for name in ten_random_names if name.startswith(char)] for char in {name[0] for name in ten_random_names}}
# print(dict_of_names)

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# for i in matrix:
#     for j in i:
#         print(j, end=" ")
# flat_odds = [j for i in matrix for j in i if j % 2 != 0]
# print(flat_odds)

# for i in range(1,6):
#     for j in range(1,11):
#         if j % 2 == 0:
#             print(i * j, end=", ")

# multiples = {
#     x: [y for y in range(x, x * 10 + 1, x) if y % 2 == 0]
#     for x in range(1, 6)
# }

# print(multiples)

# Sample text
# text = "apple banana apple cherry banana apple cherry cherry"

# # Split text into words
# words = text.split()

# # Dictionary comprehension to count word frequency
# word_count = {word: words.count(word) for word in set(words)}

# print(word_count)

# students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("Alice", 90), ("Bob", 88)]

# student_dict = {name: [score for student, score in students if name == student] for name, _ in students}

# print(student_dict)

# Normal function:

def simple_func(parameter):
    print(parameter)

# simple_func("Python")

# Higher Order Function:
# takes a function as an argument or returns a function as a result

# def higher_order(func,value):
#     return func(value)

# higher_order(simple_func, "C++")

# # Higher order function with lambda

# user_input = int(input("Enter a number: "))
# squared = higher_order(lambda x: x ** 2, user_input)
# print(squared)

# MAP

# def cube(n):
#     return n ** 3

# numbers = [10,20,30,40,50]
# cubed_list = list(map(lambda x: x ** 3,numbers))
# print(cubed_list)

# FITLER

random_list = [23,5,7,8,2,45,66,11,10]
filtered = list(filter(lambda x: x % 2 == 0, random_list))
print(filtered)

data = ["wasiq", "email@gmail.com", "032123823928", "abc@yahoo.com"]

import re
def is_email(email):
    return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))

emails = list(filter(is_email,data))
print(emails)

from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda a, b: a * b, numbers)
print("Product:", product)

# practical example of reduce

student_grades = [56,34,78,31,36,90,82,79]
failed_students = reduce(lambda a, b: a + b, list(map(lambda x: 1 if x < 40 else 0, student_grades)))
print(failed_students)


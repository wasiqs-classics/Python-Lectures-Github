import datetime as dt

print(f"The current date and time is: {dt.datetime.now()}")

print(f"The current data is: {dt.date.today()}")

print(f"The time is now: {dt.datetime.now().time()}")



today = dt.date.today()
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

current_time = dt.datetime.now().time()
print("Hour:", current_time.hour)
print("Minute:", current_time.minute)
print("Second:", current_time.second)
print("Microsecond:", current_time.microsecond)

# Only date
some_date = dt.datetime(2022, 12, 28)
print(some_date)
# Date with time details
b = dt.datetime(2022, 12, 28, 23, 55, 59, 342380)
print(b)


# Using date objects
t1 = dt.date(2018, 7, 12)
t2 = dt.date(2017, 12, 23)
t3 = t1 - t2
print("Duration (days):", t3)

# Using datetime objects
t4 = dt.datetime(2018, 7, 12, 7, 9, 33)
t5 = dt.datetime(2016, 6, 10, 5, 55, 13)
t6 = t4 - t5
print("Duration:", t6)

import math

print(dir(math)) # it will tell us about everything in maths module. 


import random

option = random.randrange(0,2)

if option == 0:
    print("Its heads")
else:
    print("Its tails")

list_of_cards = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

cards_52 = list_of_cards * 4

print(cards_52)

random.shuffle(cards_52)

print(cards_52)


import string

print(string.ascii_letters)       # All ASCII letters (both uppercase and lowercase)
print(string.ascii_lowercase)     # Lowercase letters
print(string.ascii_uppercase)     # Uppercase letters
print(string.digits)              # Digits 0-9
print(string.punctuation)         # Punctuation characters

length = 12
characters = string.ascii_letters + string.digits + string.punctuation
password = ''

for _ in range(length):
    password = password + random.choice(characters)

# password = ''.join(random.choice(characters) for _ in range(length))
print(password)

import os

cwd = os.getcwd()
print("Current Working Directory:", cwd)

files = os.listdir('.')
print("Files and Directories:", files)

path = os.path.join("folder", "subfolder", "file.txt")
print("Joined Path:", path)


# user defined functions

# syntax 

def isValidEmail(address):
    if len(address) != 0:
        if "@" in address and "." in address:
            value = True
        else:
            value = False
    return value


# Calling the function

# user_email = "abc@gmail,com"

# print(isValidEmail(user_email))

# check_Email = isValidEmail(input("Enter the email: "))

# if check_Email:
#     print("Valid Email")
# else:
#     print("Invalid Email")


import random

def FourDigitPass():
    stringg = ""
    for i in range(4):
        stringg += str(random.randint(0,9))
    return stringg

pw = FourDigitPass()
print(pw)

def LargestString(*strings):
    Largest = ""
    for oneString in strings:
        if len(oneString) > len(Largest):
            Largest = oneString
    return Largest


print(LargestString("Hello", "World", "Python", "Programming"))
print(LargestString("Hello", "World", "Python", "Programming", "Hello World."))

def PrintUserDetails(**details):
    for key, value in details.items():
        print(key, ":", value)

PrintUserDetails(Name = "John", Age = 25, City = "New York", Country = "USA")
PrintUserDetails(Name="Asim", Program="BSCS")

def stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

print(stats([1, 2, 3]))  # Output: (1, 3, 6)

print(stats([10,20,30]))

def squareList(numbs):
    return [x**2 for x in numbs]

print(squareList([1, 2, 3, 4, 5]))

dbl = lambda x: x*2
print(dbl(10))

# Recursive Function

# Factorial of a number

# 4! = 4 * 3 * 2 *1  = 24
# 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720
# factorial of 0 is 1

def factorial(n):
    # base case
    if n == 0:
        return 1
    # recursive case
    else:
        return n * factorial(n-1)

# Step by step working of the above function for n = 4
# factorial(4) = 4 * 3 * 2 * 1 * 1 = 24 

# another example:

def sum_of_series(series):
    # validity check
    for i in series:
        if type(i) != int:
            return "Invalid series"
    # base case
    if len(series) == 0:
        return 0
    # recursive case
    else:
        return series[0] + sum_of_series(series[1:])
    
# Step by step working of the above function for series = [1, 2, 3, 4]
print(sum_of_series([10,20,30,40]))

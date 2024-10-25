print("program started")

print("program is running")
var = "hello"

# if only works if a certain criteria is met otherwise normal flow of the program runs
if var == 'hello1':
    print(f"value of {var} is printed")

print("this is the normal flow.")

# if - else, in this case, if the condition is not met, then "else block" runs before the normal flow.

print("program started again")

print("program is running")
var = "hello"

# if only works if a certain criteria is met otherwise normal flow of the program runs
if var == 'hello1':
    print(f"value of {var} is printed")
else:
    print("this will only run if the condition of 'if' is not true")

print("this is the normal flow.")

# if - elif - else

# scenario: if user country is UK then discount is 10%, if country is US discount is 20% if country is Pakistan discount is 40% else discount is 25%

country = "Pakistan"

if country == "UK":
    discount = 10
elif country == "US":
    discount = 20
elif country == "Pakistan":
    discount = 40
else:
    discount = 25

print(f"For the country: {country} the discount is {discount}%")

# Nested ifs - condition within condition 

age = 25
document = True

if country == "Pakistan":
    if age >= 18:
        print("You need CNIC")
    else:
        print("You need B - Form")
else:
    print("You don't need anything")

#Ternary Operator
# Single line if - else check. Shortcut for if - else. 

marks = 45    
result = "Pass" if marks >= 40 else "Fail"
print(result)

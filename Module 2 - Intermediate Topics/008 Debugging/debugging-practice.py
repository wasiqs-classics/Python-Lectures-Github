
# x = float(input("Enter value 1: "))
# y = float(input("Enter value 2: "))

# try:
#     res = x / y

# except ZeroDivisionError:
#     print("Division not possible by zero")    

# else:
#     print(f"Output is: {res}")

# ==============================
# try:
#     print(x)

# except:
#     print("Something bad has happened")

# ==================================


# try:
#     x = float(input("Enter value 1: "))
#     y = float(input("Enter value 2: "))
#     res = x / y

# except (ZeroDivisionError, ValueError) as e:
#     print(f"An error has occured: {e}")    

# else:
#     print(f"Output is: {res}")

# ====================
# try:
#    with open('data.csv') as file:
#        read_data = file.read()
# except FileNotFoundError as fnf_error:
#    print(fnf_error)
#    print("Explanation: We cannot load the 'data.csv' file")

# try:
#     result = 10/h
# except: 
#     print("Error!")
# else:
#     print("No error")
# finally:
#     print("All good")

# amount = int(input("Enter amount you want to with draw? >> "))
# if amount % 500 != 0:
#     raise ValueError("Please enter value in multiples of 500")
# else:
#     print("Successfull!")

# value = 2_000
# if value > 1_000:   
#     # raise the ValueError
#     raise ValueError("Please add a value lower than 1,000")
# else:
#     print("Congratulations! You are the winner!!")

value = 2_000
try:
    if value > 1_000:
          
        # raise the ValueError
        raise ValueError("Please add a value lower than 1,000")
    else:
        print("Congratulations! You are the winner!!")
              
# if false then raise the value error
except ValueError as e:
        print(e)
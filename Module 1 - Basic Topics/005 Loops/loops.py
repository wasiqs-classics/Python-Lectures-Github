# For loop example

users = ["Ali", "Azeem", "Shahid"]

for user in users:
    print(f"Hi, {user}!")

# printing a table

table = int(input("Enter the table you want to print: "))

for i in range(1, 11):
    print(f"{table} x {i} = {table*i}") # 2 x 1 = 2

users_db = ["Rehman", "Rayan", "Dayan", "Shayan"]

username = input("Choose your user name: ")

global user_success
user_success = True
for user in users_db:
    if user == username:
        print(f"{user} already exists in the system")
        user_success = False
        break

if user_success == True:
    print(f"{username} is successfully created.")
else:
    print("This account cannot be created")

for i in range(1, 6):
    print("*" * i)


attempts = 3
while attempts > 0:
    password = input("Enter password: ")
    if password == "secret":
        print("Access Granted")
        break
    else:
        attempts -= 1
        print(f"Incorrect password. {attempts} attempts left.")

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
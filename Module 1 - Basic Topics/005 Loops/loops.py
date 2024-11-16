# # For loop example

# users = ["Ali", "Azeem", "Shahid"]

# for user in users:
#     print(f"Hi, {user}!")

# # printing a table

# table = int(input("Enter the table you want to print: "))

# for i in range(1, 11):
#     print(f"{table} x {i} = {table*i}") # 2 x 1 = 2

# users_db = ["Rehman", "Rayan", "Dayan", "Shayan"]

# username = input("Choose your user name: ")

# global user_success
# user_success = True
# for user in users_db:
#     if user == username:
#         print(f"{user} already exists in the system")
#         user_success = False
#         break

# if user_success == True:
#     print(f"{username} is successfully created.")
# else:
#     print("This account cannot be created")

# for i in range(1, 6):
#     print("*" * i)


# attempts = 3
# while attempts > 0:
#     password = input("Enter password: ")
#     if password == "secret":
#         print("Access Granted")
#         break
#     else:
#         attempts -= 1
#         print(f"Incorrect password. {attempts} attempts left.")

# for i in range(1, 11):
#     if i % 2 == 0:
#         continue
#     print(i)

# for i in range(1, 10):
#     if i == 5:
#         continue # skip the current iteration
#     if i == 7:
#         break # stops the loop
#     print(i)

# for i in range(1,20,2):
#     print(i)

# for i in range(10,1, -1):
#     print(i)

# players = ["Aqib", "Javed", "Wasim", "Akram"]

# for player in players:
#     if player == "Wasim":
#         print("Player is found")
#         break
#     else:
#         print("this is another else")
# else:
#     print("Search is completed.")

# days = ["Mon", "Tues", "Wed", "Thur", "Fri", "Sat", "Sun"]
# for day in days:
#     print(f"Day is: {day}")
#     for i in range(1,25,3):
#         print(i,end=" ")
#     print("\n")

# for x in range(1,4):
#     print(f"Outer Loop Iteration: {x} >>> ")
#     for y in range(1,4):
#         print(f"Inner Loop Iteration: {y}")
#     print("----End of Outer Iteration -----")

# # Multiplication Table
# for i in range(1, 6):
#     for j in range(1, 6):
#         print(f"{i * j:2}", end=" ")
#     print()


# menu = {
#     'Burger': 5.0,
#     'Pizza': 8.0,
#     'Salad': 4.5,
#     'Water': 1.0
# }

# current_order = None
# total = 0

# while True:
#     print("\nWelcome to the Restaurant")
#     print("1. View Menu")
#     print("2. Place Order")
#     print("3. View Order")
#     print("4. Checkout")
#     print("5. Exit")
#     choice = input("Enter your choice: ")

#     if choice == '1':
#         print("\nMenu:")
#         for item, price in menu.items():
#             print(f"{item}: ${price:.2f}")
    
#     elif choice == '2':
#         item = input("\nEnter the item you want to order: ")
#         if item in menu:
#             current_order = item
#             total = menu[item]  # Update total for the current item
#             print(f"{item} added to your order.")
#         else:
#             print("Item not available.")
        
#     elif choice == '3':
#         if current_order:
#             print(f"\nYour Order: {current_order} - ${total:.2f}")
#         else:
#             print("\nYou haven't placed an order yet.")

#     elif choice == '4':
#         if current_order:
#             print(f"\nCheckout: {current_order} - ${total:.2f}")
#             print(f"Total: ${total:.2f}")
#             break  # Exit after checkout
#         else:
#             print("\nYou haven't placed an order yet.")

#     elif choice == '5':
#         print("\nThank you for visiting!")
#         break  # Exit the loop

#     else:
#         print("Invalid choice. Please enter a number between 1 and 5.")

for a in range(1,4):
    for b in range(1,4):
        print(b, end=" ")
    print()

print("Hello", end="\t")
print("World")
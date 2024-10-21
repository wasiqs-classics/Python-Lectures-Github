menu = {
    'Burger': 5.0,
    'Pizza': 8.0,
    'Salad': 4.5,
    'Water': 1.0
}

current_order = None
total = 0

while True:
    print("\nWelcome to the Restaurant")
    print("1. View Menu")
    print("2. Place Order")
    print("3. View Order")
    print("4. Checkout")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        print("\nMenu:")
        for item, price in menu.items():
            print(f"{item}: ${price:.2f}")

    elif choice == '2':
        item = input("\nEnter the item you want to order: ")
        if item in menu:
            current_order = item
            total = menu[item]  # Update total for the current item
            print(f"{item} added to your order.")
        else:
            print("Item not available.")

    elif choice == '3':
        if current_order:
            print(f"\nYour Order: {current_order} - ${total:.2f}")
        else:
            print("\nYou haven't placed an order yet.")

    elif choice == '4':
        if current_order:
            print(f"\nCheckout: {current_order} - ${total:.2f}")
            print(f"Total: ${total:.2f}")
            break  # Exit after checkout
        else:
            print("\nYou haven't placed an order yet.")

    elif choice == '5':
        print("\nThank you for visiting!")
        break  # Exit the loop

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

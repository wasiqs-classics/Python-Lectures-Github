# In this example we will try to simulate an ATM Machine Operation using Python Functions

# Funtion to start ATM and check user's validity

card_ID = "1432-1211-1911-3401"
actual_PIN = "1009"
def Welcome():
    print("Welcome to the ATM Machine")
    entered_card_ID = input("Please enter your card ID: ")
    entered_PIN = input("Please enter your PIN: ")
    
    if entered_card_ID == card_ID and entered_PIN == actual_PIN:
        print("Authentication successful!")
        # Proceed with further operations
    else:
        print("Authentication failed. Please try again.")
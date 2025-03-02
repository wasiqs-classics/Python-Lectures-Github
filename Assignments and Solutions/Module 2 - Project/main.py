from todo_module import (
    add_task,
    view_tasks,
    update_task,
    delete_task,
    extract_emails
)

# its really good to have a main function which runs the program. 

def main() -> None:
    """
    Function to run the main script
    """
    while True:
        print("\n ------ TO DO APP UPDATED ------")
        print("===================================")
        print("1. Add a new task")
        print("2. View Tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Extract emails")
        print("6. Exit")

        choice : str = input("Type 1 - 6 for the menu choice: ")

        # Act based on user's choice. 

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            emails : list = extract_emails()
            if emails:
                print("Following emails extracted: ")
                for email in emails:
                    print(f" - {email}")
            else:
                print("No emails found in tasks.")
        elif choice == "6":
           print("Exiting the program, bye!")
           break
        else:
            print("Invalid Choice, try again!")

if __name__ == "__main__":
    main()
# This is the Todo App Project for Basic Module

# Menu items
# 1. Add Task, 2. View Tasks, 3. Delete Tasks, Exit program

task_list = []
while(True):
    print()
    print("===============================")
    print("Welcome to the Task Manager App")
    print("===============================")
    print()
    print("Choose action from the Menu (Press 1,2,3 or 4)")
    print("1. Add a Task")
    print("2. View All Tasks")
    print("3. Delete Task")
    print("4. Exit")
    print()

    
    choice = input(">> ")

    if choice == '1':
        current_task = input("Enter task to be added: ")
        task_list.append(current_task)
        print(f"Task: '{current_task}' has been added to the list.")
        # print(task_list) only open it if we want to check the proper functioning
        current_task = ""
    elif choice == '2':
        print()
        print("Available Tasks")
        print("===============")
        task_numb = 1
        for task in task_list:
            print(f"{task_numb} : {task}")
            task_numb += 1

    elif choice == '3':
        print()
        delete_task = input("Enter the task you want to delete? ")
        if delete_task in task_list:
            task_list.remove(delete_task)
            print(f"Task: '{delete_task}' has been removed.")
        else:
            print(f"Task: '{delete_task}' does not exist in the list. ")
    elif choice == '4':
        break
    else:
        print("Wrong Choice")

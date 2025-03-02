from typing import List
import re

TASKS_FILE : str = "tasks.txt" # file name to store the tasks. 

def load_tasks() -> List[str]:
    """
    Function to load the tasks from the text file into a python list
    and it returns a list of tasks (string list)
    """
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks] # returns a list of tasks where for each task the whitespaces are removed.
    except FileNotFoundError:
        # if the file does not found, then return an empty list
        return []
    
def save_tasks(tasks: List[str]) -> None:
    """
    Saves the list of tasks into a file. 
    It takes a list of string as argument. 
    """
    try:
        with open(TASKS_FILE, "w") as file:
            for task in tasks:
                file.write(task + "\n")
    except Exception as e:
        print(f"Error in saving file: {e}")


def add_task() -> None:
    """
    Add a task to the list
    """
    current_task: str = input("Enter a new task: ").strip()
    if current_task:
        list_of_tasks : List[str] = load_tasks()
        list_of_tasks.append(current_task)
        save_tasks(list_of_tasks)
        print(f"Task '{current_task}' has been added to the list of tasks.")
    else:
        print("Task cannot be empty!")


def view_tasks() -> None:
    """
    Prints the list of all tasks from the file. 
    """
    list_of_tasks : List[str] = load_tasks()
    if list_of_tasks:
        print("--- Your list of tasks ---")
        for num, single_task in enumerate(list_of_tasks, start=1):
            print(f"{num} - {single_task}")
    else:
        print("Task list is empty right now!")   

def update_task() -> None:
    """
    Update a task by its reference number
    """
    list_of_tasks : List[str] = load_tasks()
    if not list_of_tasks:
        print("No task to update!")
    
    view_tasks()

    # now we will take user input to update a specific task

    try:
        task_num : int = int(input("Enter the task number to update: "))
        if 1 <= task_num <= len(list_of_tasks):
            new_task : str = input("Enter the new task: ")
            if new_task:
                list_of_tasks[task_num - 1] = new_task
                save_tasks(list_of_tasks)
                print("Task updated successfully!")
            else:
                print("The task cannot be empty!")
        else:
            print("Invalid task number. Stay in range.") 
    except ValueError:
        print("Please enter a valid number only.")  



def delete_task():
    """
    Delete a task by its reference number
    """
    list_of_tasks : List[str] = load_tasks()
    if not list_of_tasks:
        print("No task to delete!")
    
    view_tasks()

    # now we will take user input to update a specific task

    try:
        task_num : int = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(list_of_tasks):
            del_task : str = list_of_tasks.pop(task_num - 1)
            save_tasks(list_of_tasks)
            print(f"Task '{del_task}' deleted successfully!")
        else:
            print("Invalid task number. Stay in range.") 
    except ValueError:
        print("Please enter a valid number only.")

def extract_emails() -> List[str]:
    """
    Returns a list of email addresses from the tasks file (if they exist)
    """
    try: 
        # load the tasks from the file
        list_of_task : List[str] = load_tasks()
        if not list_of_task:
            print("No tasks available for email scan.")
            return []
        
        # define a pattern that represents an email address
        email_pattern : str = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        collected_emails : List[str] = []

        # iterate through each task and collect emails
        for task in list_of_task:
            found_emails : List[str] = re.findall(email_pattern, task)
            collected_emails.extend(found_emails)

        return collected_emails
    
    except Exception as e:
        print(f"Error extarcting emails. {e}")
        return []

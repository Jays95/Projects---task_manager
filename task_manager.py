import datetime
import sys
BOLD = "\033[1m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
END = "\033[0m"

# Initialize lists to store existing usernames and passwords
username = []
password = []
new_username=[]

# Read existing user data from the user.txt file
with open("user.txt", "r") as file:     `1q`
    for line in file:
        temp = line.strip().split(",")
        username.append(temp[0])
        password.append(temp[1])

# Ask the user for their login details
while True:
    Assignment_to = input("Enter your username: ")
    login_password = input("Enter your password: ")

    # Check if the entered credentials match what's stored
    if Assignment_to in username and login_password in password:
        print(f"{BOLD}Login successful{BOLD}{END}")
        break
    else:
        print("Invalid username or password")

# Admin menu (if applicable)
if Assignment_to == "admin":
    print(f"{BOLD}{YELLOW}__________Admin menu__________{END}")
    menu = '''Select one of the following options:
    r - register
    a - add task
    va - view all tasks
    vm - view my tasks
    s - statistics
    e - exit
    : '''
else:
    # Non-admin menu
    menu = ('''Select one of the following options:
    a - add task
    va - view all tasks
    vm - view my tasks
    e - exit
    : ''')

while True:
    option = input(menu)
    if option == "r":
        if Assignment_to == "admin":
            print(f"{BOLD}{YELLOW}__________Registration__________\
                {END}")
            # Admin registration logic
            new_username = input("Enter a new username: ")
            new_password = input("Enter a new password: ")
            password_confirm = input("Please confirm your password: ")

            # Check if the username already exists
            if new_username in username:
                print(f"{LIGHT_BLUE}Username already in use.Please choose a different one.{END}")
            elif new_password == password_confirm:
                with open("user.txt", "a", encoding="UTF-8") as file:
                    file.write(f"\n{new_username},{new_password.strip()}")
                    print(f"{BOLD}{LIGHT_BLUE}User registered successfully{END}")
            else:
                print(f"{LIGHT_BLUE}Passwords do not match. User not added.{END}")
        else:
            print(f"{LIGHT_BLUE}{BOLD}Only admin is allowed to register.{END}")

    elif option == "a":
        # Prompt user for task details
        task_username = input("Please enter the username of the assignee: ")
        task_title = input("Enter the task title: ")
        task_description = input("Enter the task description: ")
        task_due_date = input("Enter the due date (dd-mm-yyyy): ")
        task_date_assigned = datetime.datetime.now().strftime("%d %m %Y")
        task_completed = "No"

        # Append task to tasks.txt
        with open("tasks.txt", "a") as file:
            file.write(f"\n{task_username}, {task_title}, "
                       f"{task_description}, {task_date_assigned}, "
                       f"{task_due_date}, {task_completed}")

    elif option == "va":
        # Read tasks from tasks.txt file
        with open("tasks.txt", "r", encoding="UTF-8") as file:
            lines = file.readlines()
            for line in lines:
                split_tasks = line.strip().split(',')
                if len(split_tasks) >= 6:
                    print(f"{LIGHT_BLUE}{'_' * 100}{END}\nTask: {split_tasks[1]}")
                    print(f"Assignment to: {split_tasks[0]}")
                    print(f"Date assigned: {split_tasks[3]}")
                    print(f"Due date: {split_tasks[4]}")
                    print(f"Task completed?: {split_tasks[5]}")
                    print(f"Task description:\n{split_tasks[2]}")
                else:
                    print("Invalid data format in tasks.txt.Skipping this task.")

    elif option == 'vm':
        found_tasks = False
        with open("tasks.txt", "r", encoding="UTF-8") as file:
            for line in file:
                split_tasks = line.strip().split(',')
                if split_tasks[0] == Assignment_to:
                    print(f"{YELLOW}{'_' * 100}{END}\nTask: {line.split(',')[1]}")
                    print(f"Assignment to: {line.split(',')[0]}")
                    print(f"Date assigned: {line.split(',')[3]}")
                    print(f"Due date: {line.split(',')[4]}")
                    print(f"Task completed?: {line.split(',')[5]}")
                    print(f"Task description:\n{line.split(',')[2]}")
                    found_tasks =True

    if option == "s":
        if Assignment_to == "admin":
        # Statistics logic
            with open("user.txt", "r") as user_file:
                total_users = len(user_file.readlines())
                print(f"{BOLD}{YELLOW}__________Statistics__________{END}")  
                print(f"{LIGHT_BLUE}Total users:{END} {total_users}")
            with open("tasks.txt", "r") as tasks_file:
                total_tasks = len(tasks_file.readlines())
                print(f"{LIGHT_BLUE}Total tasks{END}: {total_tasks}")
        else:
            print(f"{LIGHT_BLUE}{BOLD}Only admin is allowed to view stats.{END}")            
            
    elif option == "e":
        print(f"{YELLOW}{BOLD}Goodbye :)  {END}")
        sys.exit(0)
    else:
        print("Invalid input. Please choose a valid menu option.")


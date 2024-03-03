# Empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print("Task added successfully!")

# Function to remove a task from the list
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task removed successfully!")
    else:
        print("Task not found.")

# Function to display all tasks in the list
def display_tasks():
    if tasks:
        print("\nTasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("\nNo tasks.")

# Main loop
while True:
    print("\n1. Add task")
    print("2. Remove task")
    print("3. Display tasks")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        task = input("Enter task to remove: ")
        remove_task(task)
    elif choice == "3":
        display_tasks()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
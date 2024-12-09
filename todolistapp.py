# To-Do List App

def display_menu():
    print("\nTo-Do List App")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Remove Task")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks in the to-do list.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "✔" if task["done"] else "✘"
            print(f"{i}. {task['name']} [{status}]")

def add_task(tasks):
    task_name = input("\nEnter the task: ")
    tasks.append({"name": task_name, "done": False})
    print("Task added successfully!")

def mark_task_done(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("\nEnter the task number to mark as done: "))
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("\nEnter the task number to remove: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task['name']}' removed!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                view_tasks(tasks)
            elif choice == 2:
                add_task(tasks)
            elif choice == 3:
                mark_task_done(tasks)
            elif choice == 4:
                remove_task(tasks)
            elif choice == 5:
                print("Exiting the app. Have a productive day!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()

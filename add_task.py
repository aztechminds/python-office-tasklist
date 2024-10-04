from datetime import datetime, timedelta

tasks = []

def add_task():
    task = input("Type a new task: \n")
    due_date = input("enter an expiry date for the task: \n")

    tasks.append({"task": task, "due_date": due_date})

    print(f"{task} with due date {due_date} added to your office tasklist.")

def show_tasklist():
    if not tasks:
        print("Your Tasklist is empty!")
        return
    today = datetime.now()
    for task in tasks:
        task_name = task["task"]
        due_date_str = task["due_date"]
        due_date = datetime.strptime(due_date_str, "%d.%m.%Y")
        days_until_due = (due_date - today).days

        if days_until_due <= 2:
            print(f"\033[91m- Task: {task_name}, Due Date: {due_date_str} ({days_until_due} remaining Days)\033[0m")
        else:
            print(f"- Task: {task_name}, Due date: {due_date_str} ({days_until_due} remain Days)")

def remove_task():
    show_tasklist()

    if not tasks:
        return
    
    try:
        task_number = int(input("enter number of the task, you wish to remove: \n"))

        if 1 <= task_number <= len(tasks):
            remove_task = tasks.pop(task_number - 1)
            print(f"The task '{remove_task['task']}' has been removed.")
        else:
            print("enter a valid number: \n")
    except ValueError:
        print("Please enter a valid number. \n")

def main():
    while True:
        print("\nWhat do you want to do?")
        print("1. New Task")
        print("2. Show tasklist")
        print("3. Remove a task")
        print("4. Exit")

        choice = input("Please enter a number: \n")

        if choice == '1':
            add_task()
        elif choice == '2':
            show_tasklist()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Tasklist programm closed!")
            break
    else:
        print("Not a valid number, please choose from 1 to 4.")
        

if __name__ == "__main__":
    main()
     





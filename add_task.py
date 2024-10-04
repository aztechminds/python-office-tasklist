from datetime import datetime, timedelta

tasks = []

def add_task():
    task = input("Type a new task: \n")
    due_date = input("enter an expiry date for the task: \n")

    tasks.append({"task": task, "due_date": due_date})

    print(f"{task} with due date {due_date} added to your office tasklist")

def show_tasklist():
    if not tasks:
        print("current tasklist")
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

        
if __name__ == "__main__":
    add_task()
    print("Here is your tasklist:")
    show_tasklist()





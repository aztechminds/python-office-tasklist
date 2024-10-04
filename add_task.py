tasks = []

def add_task():
    task = input("Type a new task: \n")
    due_date = input("enter an expiry date for the task: \n")
    tasks.append({"task": task, "due_date": due_date})
    print(f"{task} with due date {due_date} added to your office tasklist")

if __name__ == "__main__":
    add_task()





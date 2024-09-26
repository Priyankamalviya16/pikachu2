import json
import os

# File to store tasks
TASKS_FILE = 'tasks.json'

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f)

# Add a task
def add_task(tasks, task):
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for index, task in enumerate(tasks):
        status = "✔" if task['completed'] else "✘"
        print(f"{index + 1}. [{status}] {task['task']}")

# Delete a task
def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
    else:
        print("Invalid task number.")

# Mark a task as completed
def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True
        save_tasks(tasks)
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Complete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(tasks, index)
        elif choice == '4':
            index = int(input("Enter task number to complete: ")) - 1
            complete_task(tasks, index)
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

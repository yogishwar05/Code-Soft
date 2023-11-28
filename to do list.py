import os
import json
from datetime import datetime

class ToDoList:
    def __init__(self, filename='todolist.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        else:
            return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=2)

    def show_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task['title']} ({task['date']})")

    def add_task(self, title):
        new_task = {'title': title, 'date': str(datetime.now())}
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Task '{title}' added successfully.")

    def remove_task(self, index):
        if 1 <= index <= len(self.tasks):
            removed_task = self.tasks.pop(index - 1)
            self.save_tasks()
            print(f"Task '{removed_task['title']}' removed successfully.")
        else:
            print("Invalid task index.")

    def clear_tasks(self):
        self.tasks = []
        self.save_tasks()
        print("All tasks cleared.")

# Main function
def main():
    todo_list = ToDoList()

    while True:
        print("\nTO-DO LIST MENU:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Clear All Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            todo_list.show_tasks()
        elif choice == '2':
            title = input("Enter task title: ")
            todo_list.add_task(title)
        elif choice == '3':
            index = int(input("Enter the index of the task to remove: "))
            todo_list.remove_task(index)
        elif choice == '4':
            todo_list.clear_tasks()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

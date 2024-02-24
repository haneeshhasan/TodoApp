class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added:", task)

    def view_tasks(self):
        if self.tasks:
            print("Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("No tasks.")

    def complete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            completed_task = self.tasks.pop(task_number - 1)
            print("Completed task:", completed_task)
        else:
            print("Invalid task number.")

    def remove_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print("Removed task:", removed_task)
        else:
            print("Invalid task number.")


def main():
    todo_list = TodoList()

    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_number = int(input("Enter task number to complete: "))
            todo_list.complete_task(task_number)
        elif choice == "4":
            task_number = int(input("Enter task number to remove: "))
            todo_list.remove_task(task_number)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()

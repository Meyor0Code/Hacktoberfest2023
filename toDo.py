# todo.py

# i defined a list to store tasks
tasks = []

# function to add a task
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added!")

# Function to list tasks
def list_tasks():
    if not tasks:
        print("No tasks to display.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Function to mark a task as done
def mark_done(task_index):
    if 1 <= task_index <= len(tasks):
        task = tasks[task_index - 1]
        print(f"Task '{task}' marked as done!")
    else:
        print("Invalid task index. Please provide a valid task number.")

# Function to delete a task
def delete_task(task_index):
    if 1 <= task_index <= len(tasks):
        task = tasks.pop(task_index - 1)
        print(f"Task '{task}' deleted!")
    else:
        print("Invalid task index. Please provide a valid task number.")

# Main function to interact with the user
def main():
    while True:
        print("\nOptions:")
        print("1. Add a task")
        print("2. List tasks")
        print("3. Mark a task as done")
        print("4. Delete a task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            task_index = int(input("Enter the task number to mark as done: "))
            mark_done(task_index)
        elif choice == "4":
            task_index = int(input("Enter the task number to delete: "))
            delete_task(task_index)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

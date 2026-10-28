
from task import Task
from storage import load_tasks, save_tasks


def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return

    print("\n--- Your Study Tasks ---")

    for number, task in enumerate(tasks, start=1):
        if task.done:
            status = "Done"
        else:
            status = "Not done"

        print(f"{number}. {task.title} - {status}")


def add_task(tasks):
    title = input("Enter task name: ").strip()

    if not title:
        print("Task name cannot be blank.")
        return

    tasks.append(Task(title))
    print("Task added successfully.")


def complete_task(tasks):
    show_tasks(tasks)

    if not tasks:
        return

    choice = input("Enter task number to complete: ").strip()

    try:
        number = int(choice)
    except ValueError:
        print("Please enter a valid number.")
        return

    if number < 1 or number > len(tasks):
        print("Task number does not exist.")
        return

    tasks[number - 1].mark_done()
    print("Task marked as Done.")


def main():
    tasks = load_tasks()

    if tasks is None:
        print("Please fix tasks.json before continuing.")
        return

    while True:
        print("\n===== EnjoyStudying =====")
        print("1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Save and exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            save_tasks(tasks)
            break

        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()

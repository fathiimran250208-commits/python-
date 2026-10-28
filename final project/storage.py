
import json
from pathlib import Path
from task import Task

FILE_PATH = Path(__file__).with_name("tasks.json")


def load_tasks():
    if not FILE_PATH.exists():
        return []

    try:
        with FILE_PATH.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            print("Error: tasks.json must contain a list.")
            return None

        tasks = []

        for item in data:
            if not isinstance(item, dict):
                print("Error: Invalid task data.")
                return None

            title = item.get("title")
            done = item.get("done", False)

            if (
                not isinstance(title, str)
                or not title.strip()
                or not isinstance(done, bool)
            ):
                print("Error: Invalid task data.")
                return None

            tasks.append(Task(title, done))

        return tasks

    except (OSError, json.JSONDecodeError, UnicodeError) as error:
        print("Could not load tasks:", error)
        return None


def save_tasks(tasks):
    data = []

    for task in tasks:
        data.append({
            "title": task.title,
            "done": task.done
        })

    try:
        with FILE_PATH.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print("Tasks saved successfully.")

    except (OSError, TypeError, ValueError) as error:
        print("Could not save tasks:", error)

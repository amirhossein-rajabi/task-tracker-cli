import json
import os

TASKS_FILE = "tasks.json"


def initialize_storage():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w") as file:
            json.dump([], file)


def load_tasks():
    initialize_storage()

    try:
        with open(TASKS_FILE, "r") as file:
            content = file.read().strip()

            if not content:
                return []

            return json.loads(content)

    except json.JSONDecodeError:
        return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)
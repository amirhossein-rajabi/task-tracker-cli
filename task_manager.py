"""
Task Manager Module
Handles all business logic for task operations.
"""

from datetime import datetime
from storage import load_tasks, save_tasks


def add_task(description: str) -> None:
    """
    Add a new task to the system.

    Args:
        description (str): Description of the task
    """
    tasks = load_tasks()

    new_id = 1 if len(tasks) == 0 else tasks[-1]["id"] + 1
    now = datetime.now().isoformat()

    new_task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added with id {new_id}")


def list_tasks(filter_status: str = None) -> None:
    """
    List all tasks, optionally filtered by status.

    Args:
        filter_status (str, optional): Filter by 'todo', 'in-progress', or 'done'
    """
    tasks = load_tasks()

    if filter_status:
        tasks = [t for t in tasks if t["status"] == filter_status]

    if not tasks:
        print("No tasks found")
        return

    for task in tasks:
        print("-" * 40)
        print(f"ID          : {task['id']}")
        print(f"Description : {task['description']}")
        print(f"Status      : {task['status']}")
        print(f"Created     : {task['createdAt']}")
        print(f"Updated     : {task['updatedAt']}")
    print("-" * 40)


def update_task(task_id: int, new_description: str) -> None:
    """Update the description of an existing task."""
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print("Task updated")
            return

    print("Task not found")


def delete_task(task_id: int) -> None:
    """Delete a task by its ID."""
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]

    if len(tasks) == len(new_tasks):
        print("Task not found")
        return

    save_tasks(new_tasks)
    print("Task deleted")


def mark_task(task_id: int, status: str) -> None:
    """
    Mark a task with a specific status.

    Args:
        task_id (int): ID of the task
        status (str): 'todo', 'in-progress', or 'done'
    """
    tasks = load_tasks()
    valid_statuses = ["todo", "in-progress", "done"]

    if status not in valid_statuses:
        print("Invalid status")
        return

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task marked as {status}")
            return

    print("Task not found")
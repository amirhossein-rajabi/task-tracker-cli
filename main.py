import sys

from task_manager import (
    add_task,
    list_tasks,
    update_task,
    delete_task,
    mark_task
)


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>")
        return

    command = sys.argv[1]

    try:

        if command == "add":
            if len(sys.argv) < 3:
                print("Please provide task description")
                return

            add_task(sys.argv[2])

        elif command == "list":
            if len(sys.argv) == 2:
                list_tasks()
            else:
                list_tasks(sys.argv[2])

        elif command == "update":
            if len(sys.argv) < 4:
                print("Usage: update <id> <description>")
                return

            task_id = int(sys.argv[2])
            update_task(task_id, sys.argv[3])

        elif command == "delete":
            if len(sys.argv) < 3:
                print("Usage: delete <id>")
                return

            task_id = int(sys.argv[2])
            delete_task(task_id)

        elif command == "mark-done":
            task_id = int(sys.argv[2])
            mark_task(task_id, "done")

        elif command == "mark-in-progress":
            task_id = int(sys.argv[2])
            mark_task(task_id, "in-progress")

        else:
            print("Unknown command")

    except ValueError:
        print("Task ID must be a number")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
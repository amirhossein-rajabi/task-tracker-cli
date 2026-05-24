# Task Tracker CLI

A simple command line task manager built with Python.

## Features

- Add tasks
- Update tasks
- Delete tasks
- Mark tasks as done or in progress
- List tasks with filters (todo, done, in-progress)
- Persistent storage using JSON file

## How to Run

### Add task
python main.py add "Buy groceries"

### List tasks
python main.py list
python main.py list done
python main.py list todo
python main.py list in-progress


### Update task
python main.py update 1 "New description"

### Delete task
python main.py delete 1


### Mark task status
python main.py mark-done 1
python main.py mark-in-progress 1


## Project Structure
task_tracker/
│
├── main.py
├── task_manager.py
├── storage.py
├── tasks.json
└── README.md


## Notes
- No external libraries used
- Data stored locally in JSON file
- Built using Python standard library only
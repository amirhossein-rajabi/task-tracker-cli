# Task Tracker CLI

A simple yet powerful Command Line Interface (CLI) tool for managing and tracking your tasks, built with **Python**.

This project helps you register tasks, track their status, and manage them efficiently without needing a graphical interface.

---

## ✨ Features

- Add new tasks
- Update task descriptions
- Delete tasks
- Mark tasks with different statuses (`todo`, `in-progress`, `done`)
- List all tasks with filters (all, done, todo, in-progress)
- Persistent storage using a JSON file
- Built using only Python standard libraries (no external dependencies)

---

## 📁 Project Structure

```
task-tracker-cli/
├── main.py                 # Main entry point and CLI handler
├── task_manager.py         # Core task management logic
├── storage.py              # JSON file read/write operations
├── tasks.json              # Data storage file (auto-created)
├── .gitignore              # Git ignore rules
└── README.md
```

---

## 🚀 Installation & Usage

Make sure you have **Python 3.6+** installed.

Clone the repository or navigate to the project folder and run commands as follows:

### Adding a Task
```bash
python main.py add "Buy groceries"
```

### Listing Tasks
```bash
python main.py list              # Show all tasks
python main.py list todo
python main.py list in-progress
python main.py list done
```

### Updating a Task
```bash
python main.py update 1 "Buy groceries and cook dinner"
```

### Deleting a Task
```bash
python main.py delete 1
```

### Marking Status
```bash
python main.py mark-in-progress 1
python main.py mark-done 1
```

---

## 📋 Task Structure

Each task in `tasks.json` has the following structure:

```json
{
  "id": 1,
  "description": "Buy groceries",
  "status": "todo",
  "createdAt": "2026-06-13T09:00:00.000000",
  "updatedAt": "2026-06-13T09:05:00.000000"
}
```

---

## 🛠️ Improvements Made

- Professional and well-structured README in proper Markdown
- Clear instructions and usage examples
- Complete coverage of all features
- Ready for adding `requirements.txt` and tests

---

## 📌 Important Notes

- The program automatically creates `tasks.json` if it doesn't exist.
- Proper error handling for invalid IDs and edge cases.
- No external libraries are used.

---

## 🔮 Future Improvements

1. Create `requirements.txt` (even if empty)
2. Add unit tests using Python's `unittest`
3. Make it installable as a CLI tool
4. Add search functionality
5. Optional colored output

---

## 📄 License

This project is licensed under the MIT License.

---



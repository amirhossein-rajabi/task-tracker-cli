"""
Storage Module
Handles all file operations for saving and loading tasks using JSON.
"""

import json
import os
from datetime import datetime


def initialize_storage(filename: str = "tasks.json") -> None:
    """Initialize the tasks.json file if it doesn't exist."""
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump([], f, indent=2, ensure_ascii=False)
        print(f"Initialized {filename}")


def load_tasks(filename: str = "tasks.json") -> list:
    """Load tasks from JSON file."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(tasks: list, filename: str = "tasks.json") -> None:
    """Save tasks to JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)
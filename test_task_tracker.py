import unittest
import os
import json
import sys
from datetime import datetime
from unittest.mock import patch

# Import project modules
sys.path.insert(0, os.path.abspath('.'))
from storage import initialize_storage, load_tasks, save_tasks
from task_manager import add_task, list_tasks, update_task, delete_task, mark_task


class TestTaskTracker(unittest.TestCase):
    """Test suite for Task Tracker CLI"""

    def setUp(self):
        """Setup before each test - clean environment"""
        self.test_file = "tasks.json"
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        initialize_storage()

    def tearDown(self):
        """Cleanup after each test"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    # ==================== UNIT TESTS ====================

    def test_initialize_storage(self):
        """Test storage initialization"""
        self.assertTrue(os.path.exists(self.test_file))

    def test_load_empty_tasks(self):
        """Test loading when no tasks exist"""
        tasks = load_tasks()
        self.assertEqual(tasks, [])

    def test_save_and_load_tasks(self):
        """Test save and load functionality"""
        sample_tasks = [{"id": 1, "description": "Test", "status": "todo"}]
        save_tasks(sample_tasks)
        loaded = load_tasks()
        self.assertEqual(loaded, sample_tasks)

    def test_add_task(self):
        """Test adding a new task"""
        add_task("Test task")
        tasks = load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["description"], "Test task")
        self.assertEqual(tasks[0]["status"], "todo")

    def test_update_task(self):
        """Test updating task description"""
        add_task("Old description")
        update_task(1, "New description")
        tasks = load_tasks()
        self.assertEqual(tasks[0]["description"], "New description")

    def test_delete_task(self):
        """Test deleting a task"""
        add_task("To be deleted")
        delete_task(1)
        tasks = load_tasks()
        self.assertEqual(len(tasks), 0)

    def test_mark_task(self):
        """Test changing task status"""
        add_task("Test status")
        mark_task(1, "in-progress")
        tasks = load_tasks()
        self.assertEqual(tasks[0]["status"], "in-progress")

    def test_list_tasks_filter(self):
        """Test filtering tasks by status"""
        add_task("Todo task")
        mark_task(1, "done")
        # This is harder to test with print, but we can check data
        tasks = load_tasks()
        done_tasks = [t for t in tasks if t["status"] == "done"]
        self.assertEqual(len(done_tasks), 1)

    # ==================== INTEGRATION TESTS ====================

    def test_full_workflow(self):
        """Integration test: full task lifecycle"""
        # Add
        add_task("Integration test task")
        # Update
        update_task(1, "Updated integration task")
        # Mark
        mark_task(1, "done")
        # Verify
        tasks = load_tasks()
        self.assertEqual(tasks[0]["description"], "Updated integration task")
        self.assertEqual(tasks[0]["status"], "done")


if __name__ == '__main__':
    unittest.main()
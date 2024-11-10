# task_manager/app.py

import tkinter as tk
from .task_list import TaskList
from .ui import TaskManagerUI

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Task Manager')

        self.task_list = TaskList()
        self.ui = TaskManagerUI(self.root, self.task_list, self.update_task_list)

        self.update_task_list()  # Ensure the task list is updated on startup

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def update_task_list(self):
        self.ui.update_task_list()

    def on_closing(self):
        self.task_list.save_tasks()
        self.root.destroy()
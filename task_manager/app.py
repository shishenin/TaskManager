import tkinter as tk
from .task_list import TaskList
from .ui import TaskManagerUI

class TaskManagerApp:
    """
    Главный класс приложения для управления задачами.
    """

    def __init__(self, root):
        """
        Инициализирует приложение, загружает список задач и создаёт пользовательский интерфейс.

        :param root: Главный контейнер tkinter.
        """
        self.root = root
        self.root.title('Task Manager')

        self.task_list = TaskList()
        self.ui = TaskManagerUI(self.root, self.task_list, self.update_task_list)

        self.update_task_list()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def update_task_list(self):
        """
        Обновляет отображение списка задач в интерфейсе.
        """
        self.ui.update_task_list()

    def on_closing(self):
        """
        Сохраняет задачи и закрывает приложение.
        """
        self.task_list.save_tasks()
        self.root.destroy()
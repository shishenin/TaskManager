import tkinter as tk
from datetime import datetime, time
from task_manager.dialog_visualizer import DialogVisualizer
from task_manager.task import Task

class TaskDialog:
    """
    Класс TaskDialog отвечает за создание, редактирование и удаление задач через диалоговое окно.

    :param parent: Родительский tkinter-контейнер.
    :param task_list: Список задач (объект класса TaskList).
    :param callback: Функция обратного вызова для обновления интерфейса.
    :param task: Задача для редактирования (Task), если None — создаётся новая задача.
    """

    def __init__(self, parent, task_list, callback, task=None):
        """
        Инициализация TaskDialog.

        Создаёт графический интерфейс для ввода или редактирования задачи, используя DialogVisualizer.

        :param parent: Родительский контейнер (tkinter).
        :param task_list: Список задач.
        :param callback: Функция для обновления внешнего интерфейса.
        :param task: Существующая задача для редактирования (или None для создания новой задачи).
        """
        self.parent = parent
        self.task_list = task_list
        self.callback = callback
        self.task = task

        # Создание диалога через визуализатор
        self.dialog, self.widgets = DialogVisualizer.create_dialog(parent, task)

        # Настройка кнопок
        self.widgets["save_button"].config(command=self.save_task)
        if task:
            self.widgets["delete_button"].config(command=self.delete_task)

    def save_task(self):
        """
        Сохраняет задачу.

        Если задача уже существует, обновляет её поля. Если задача новая, создаёт её
        и добавляет в список задач. После сохранения вызывает callback для обновления
        интерфейса и закрывает диалог.
        """
        title = self.widgets["title_entry"].get()
        description = self.widgets["description_text"].get("1.0", tk.END).strip()
        deadline = None
        if not self.widgets["deadline_var"].get():
            date = self.widgets["deadline_entry"].get_date()
            hour = int(self.widgets["hour_spinbox"].get())
            minute = int(self.widgets["minute_spinbox"].get())
            deadline = datetime.combine(date, time(hour, minute))

        if self.task:
            self.task.title = title
            self.task.description = description
            self.task.deadline = deadline
        else:
            new_task = Task(title, description, deadline, False)
            self.task_list.add_task(new_task)

        self.callback()
        self.dialog.destroy()

    def delete_task(self):
        """
        Удаляет задачу.
        """
        if self.task:
            self.task_list.tasks.remove(self.task)
            self.callback()
            self.dialog.destroy()
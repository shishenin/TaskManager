import tkinter as tk
from tkinter import ttk, messagebox
from .task_dialog import TaskDialog


class TaskManagerUI:
    """
    Класс TaskManagerUI отвечает за графический интерфейс.

    :param root: Главный tkinter-контейнер.
    :param task_list: Список задач (объект класса TaskList).
    :param update_task_list_callback: Функция обратного вызова для обновления списка задач.
    """

    def __init__(self, root, task_list, update_task_list_callback):
        """
        Инициализация интерфейса TaskManagerUI.
        """
        self.root = root
        self.task_list = task_list
        self.update_task_list_callback = update_task_list_callback

        self.setup_ui()

    def setup_ui(self):
        """
        Настраивает основные элементы графического интерфейса.
        """
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=1)

        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.sort_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='Sort', menu=self.sort_menu)
        self.sort_menu.add_command(label='By Completion', command=lambda: self.sort_tasks('completed'))
        self.sort_menu.add_command(label='By Title', command=lambda: self.sort_tasks('title'))
        self.sort_menu.add_command(label='By Deadline', command=lambda: self.sort_tasks('deadline'))

        self.tree = ttk.Treeview(self.frame, columns=('completed', 'title', 'deadline'), show='headings')
        self.tree.heading('completed', text='Completed', command=lambda: self.sort_tasks('completed'))
        self.tree.heading('title', text='Task', command=lambda: self.sort_tasks('title'))
        self.tree.heading('deadline', text='Deadline', command=lambda: self.sort_tasks('deadline'))
        self.tree.column('completed', width=80, anchor='center')
        self.tree.column('title', width=200)
        self.tree.column('deadline', width=200)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        self.scrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree.bind('<Double-1>', self.edit_task)
        self.tree.bind('<ButtonRelease-1>', self.toggle_task_completion)
        self.tree.bind('<Delete>', self.delete_task)

        self.add_button = tk.Button(self.root, text='Add Task', command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.delete_button = tk.Button(self.root, text='Delete Task', command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=5, pady=5)

    def add_task(self):
        """
        Открывает окно добавления новой задачи.
        """
        TaskDialog(self.root, self.task_list, self.update_task_list_callback)

    def edit_task(self, event):
        """
        Открывает окно редактирования выбранной задачи.

        :param event: Событие tkinter.
        """
        selected_item = self.tree.selection()
        if selected_item:
            index = int(selected_item[0])
            task = self.task_list.tasks[index]
            TaskDialog(self.root, self.task_list, self.update_task_list_callback, task=task)
        else:
            messagebox.showwarning('Warning', 'Select a task to edit.')

    def delete_task(self, event=None):
        """
        Удаляет выбранную задачу из списка.

        :param event: Событие tkinter (по умолчанию None).
        """
        selected_item = self.tree.selection()
        if selected_item:
            index = int(selected_item[0])
            self.task_list.tasks.pop(index)
            self.update_task_list_callback()
        else:
            messagebox.showwarning('Warning', 'Select a task to delete.')

    def toggle_task_completion(self, event):
        """
        Переключает статус выполнения задачи.

        :param event: Событие tkinter.
        """
        selected_item = self.tree.selection()
        if selected_item:
            index = int(selected_item[0])
            task = self.task_list.tasks[index]
            region = self.tree.identify_region(event.x, event.y)
            column = self.tree.identify_column(event.x)
            if column == '#1':
                task.completed = not task.completed
                self.update_task_list_callback()

    def update_task_list(self):
        """
        Обновляет отображение списка задач в интерфейсе.
        """
        for item in self.tree.get_children():
            self.tree.delete(item)

        for index, task in enumerate(self.task_list.tasks):
            deadline = task.deadline.strftime('%d.%m.%Y %H:%M') if task.deadline else 'No Deadline'
            completed = '✔' if task.completed else '✖'
            self.tree.insert('', 'end', iid=index, values=(completed, task.title, deadline))

    def sort_tasks(self, key):
        """
        Сортирует список задач по указанному ключу.

        :param key: Ключ для сортировки.
        """
        reverse = False
        if key == 'completed':
            self.task_list.tasks.sort(key=lambda task: task.completed, reverse=reverse)
        elif key == 'title':
            self.task_list.tasks.sort(key=lambda task: task.title.lower(), reverse=reverse)
        elif key == 'deadline':
            self.task_list.tasks.sort(key=lambda task: (task.deadline is None, task.deadline), reverse=reverse)
        self.update_task_list()
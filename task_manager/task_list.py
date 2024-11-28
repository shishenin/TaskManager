import json
from .task import Task

class TaskList:
    """
    Класс TaskList управляет списком задач, поддерживая их сохранение и загрузку в файл.

    :param SAVE_FILE_PATH: Путь к JSON-файлу для сохранения и загрузки задач.
    """

    SAVE_FILE_PATH = 'tasks.json'

    def __init__(self):
        """
        Инициализация TaskList.

        Загружает список задач из файла при создании объекта.
        """
        self.tasks = []
        self.load_tasks()

    def add_task(self, task):
        """
        Добавляет задачу в список и сохраняет его.

        :param task: Экземпляр Task, который нужно добавить.
        """
        self.tasks.append(task)
        self.save_tasks()

    def save_tasks(self):
        """
        Сохраняет текущий список задач в JSON-файл.
        """
        tasks_data = [task.to_dict() for task in self.tasks]
        with open(self.SAVE_FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump(tasks_data, f, ensure_ascii=False, indent=4)

    def load_tasks(self):
        """
        Загружает задачи из JSON-файла.

        Если файл отсутствует, создаётся пустой список задач.
        """
        try:
            with open(self.SAVE_FILE_PATH, 'r', encoding='utf-8') as f:
                tasks_data = json.load(f)
                self.tasks = [Task.from_dict(data) for data in tasks_data]
        except FileNotFoundError:
            self.tasks = []
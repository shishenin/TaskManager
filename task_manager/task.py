from datetime import datetime

class Task:
    def __init__(self, title, description, deadline=None, completed=False):
        """
        Инициализация задачи.

        :param title: Название задачи
        :param description: Описание задачи
        :param deadline: Срок выполнения (datetime), (None по умолчанию)
        :param completed: Статус выполнения задачи (False по умолчанию)
        """
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = completed

    def to_dict(self):
        """
        Преобразование задачи в словарь для сохранения в JSON.
        """
        return {
            'title': self.title,
            'description': self.description,
            'deadline': self.deadline.isoformat() if self.deadline else None,
            'completed': self.completed
        }

    @staticmethod
    def from_dict(data):
        """
        Создание экземпляра Task из словаря.

        :param data: Словарь с данными о задаче
        :return: Экземпляр Task
        """
        deadline = datetime.fromisoformat(data['deadline']) if data['deadline'] else None
        return Task(
            data['title'],
            data['description'],
            deadline,
            data['completed']
        )

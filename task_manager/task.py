# task_manager/task.py

from datetime import datetime

class Task:
    def __init__(self, title, description, deadline, completed):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = completed

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'deadline': self.deadline.isoformat() if self.deadline else None,
            'completed': self.completed
        }

    @classmethod
    def from_dict(cls, data):
        deadline = datetime.fromisoformat(data['deadline']) if data['deadline'] else None
        return cls(data['title'], data['description'], deadline, data['completed'])
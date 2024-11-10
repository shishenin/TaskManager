# task_manager/tag.py

class Tag:
    def __init__(self, name):
        self.name = name.strip('#')

    def __str__(self):
        return f'#{self.name}'

    def __eq__(self, other):
        return self.name == other.name

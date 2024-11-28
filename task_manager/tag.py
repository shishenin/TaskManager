class Tag:
    """
    Класс для представления тега.

    :param name: Имя тега (без символа '#').
    """
    def __init__(self, name):
        """Удаляет символ '#' из начала имени, если он есть."""
        self.name = name.strip('#')

    def __str__(self):
        """Возвращает тег в формате '#<name>'."""
        return f'#{self.name}'

    def __eq__(self, other):
        """Сравнивает теги по имени."""
        return isinstance(other, Tag) and self.name == other.name
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

class DialogVisualizer:
    """
    Класс DialogVisualizer отвечает за создание графических элементов для диалогового окна задачи.
    """

    @staticmethod
    def create_dialog(parent, task=None):
        """
        Создаёт диалоговое окно для добавления или редактирования задачи.

        :param parent: Родительский контейнер tkinter, в котором будет отображаться диалог.
        :param task: Объект Task (если None, диалог создаётся для новой задачи).
        :return: Кортеж (диалоговое окно, словарь виджетов).
        """
        dialog = tk.Toplevel(parent)
        dialog.title('Task')

        # Визуальные элементы
        title_label = tk.Label(dialog, text='Title:')
        title_label.grid(row=0, column=0, padx=10, pady=10)
        title_entry = tk.Entry(dialog)
        title_entry.grid(row=0, column=1, padx=10, pady=10)

        description_label = tk.Label(dialog, text='Description:')
        description_label.grid(row=1, column=0, padx=10, pady=10)
        description_text = tk.Text(dialog, height=10, width=40)
        description_text.grid(row=1, column=1, padx=10, pady=10, columnspan=4)

        deadline_var = tk.BooleanVar()
        deadline_check = tk.Checkbutton(dialog, text='No Deadline', variable=deadline_var)
        deadline_check.grid(row=2, column=0, padx=10, pady=10)

        deadline_label = tk.Label(dialog, text='Deadline:')
        deadline_label.grid(row=3, column=0, padx=10, pady=10)
        deadline_entry = DateEntry(dialog, date_pattern='dd.mm.yyyy')
        deadline_entry.grid(row=3, column=1, padx=10, pady=10)

        time_label = tk.Label(dialog, text='Time:')
        time_label.grid(row=3, column=2, padx=10, pady=10)
        hour_spinbox = tk.Spinbox(dialog, from_=0, to=23, width=2, format='%02.0f')
        hour_spinbox.grid(row=3, column=3, padx=5, pady=10)
        minute_spinbox = tk.Spinbox(dialog, from_=0, to=59, width=2, format='%02.0f')
        minute_spinbox.grid(row=3, column=4, padx=5, pady=10)

        save_button = tk.Button(dialog, text='Save')
        save_button.grid(row=4, column=0, columnspan=2, pady=10)

        delete_button = None
        if task:
            delete_button = tk.Button(dialog, text='Delete')
            delete_button.grid(row=4, column=2, columnspan=2, pady=10)

        # Возврат всех элементов
        return dialog, {
            "title_entry": title_entry,
            "description_text": description_text,
            "deadline_var": deadline_var,
            "deadline_entry": deadline_entry,
            "hour_spinbox": hour_spinbox,
            "minute_spinbox": minute_spinbox,
            "save_button": save_button,
            "delete_button": delete_button
        }
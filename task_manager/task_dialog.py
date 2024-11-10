# task_manager/task_dialog.py

import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime, time
from task_manager.task import Task

class TaskDialog:
    def __init__(self, parent, task_list, callback, task=None):
        self.parent = parent
        self.task_list = task_list
        self.callback = callback
        self.task = task

        self.dialog = tk.Toplevel(parent)
        self.dialog.title('Task')

        self.title_label = tk.Label(self.dialog, text='Title:')
        self.title_label.grid(row=0, column=0, padx=10, pady=10)
        self.title_entry = tk.Entry(self.dialog)
        self.title_entry.grid(row=0, column=1, padx=10, pady=10)

        self.description_label = tk.Label(self.dialog, text='Description:')
        self.description_label.grid(row=1, column=0, padx=10, pady=10)
        self.description_text = tk.Text(self.dialog, height=10, width=40)
        self.description_text.grid(row=1, column=1, padx=10, pady=10, columnspan=4)

        self.deadline_var = tk.BooleanVar()
        self.deadline_check = tk.Checkbutton(self.dialog, text='No Deadline', variable=self.deadline_var, command=self.toggle_deadline)
        self.deadline_check.grid(row=2, column=0, padx=10, pady=10)

        self.deadline_label = tk.Label(self.dialog, text='Deadline:')
        self.deadline_label.grid(row=3, column=0, padx=10, pady=10)
        self.deadline_entry = DateEntry(self.dialog, date_pattern='dd.mm.yyyy')
        self.deadline_entry.grid(row=3, column=1, padx=10, pady=10)

        self.time_label = tk.Label(self.dialog, text='Time:')
        self.time_label.grid(row=3, column=2, padx=10, pady=10)
        self.hour_spinbox = tk.Spinbox(self.dialog, from_=0, to=23, width=2, format='%02.0f')
        self.hour_spinbox.grid(row=3, column=3, padx=5, pady=10)
        self.minute_spinbox = tk.Spinbox(self.dialog, from_=0, to=59, width=2, format='%02.0f')
        self.minute_spinbox.grid(row=3, column=4, padx=5, pady=10)

        if self.task:
            self.title_entry.insert(0, self.task.title)
            self.description_text.insert(tk.END, self.task.description)
            if self.task.deadline:
                self.deadline_var.set(False)
                self.deadline_entry.set_date(self.task.deadline)
                self.hour_spinbox.delete(0, tk.END)
                self.hour_spinbox.insert(0, self.task.deadline.strftime('%H'))
                self.minute_spinbox.delete(0, tk.END)
                self.minute_spinbox.insert(0, self.task.deadline.strftime('%M'))
            else:
                self.deadline_var.set(True)
                self.toggle_deadline()

        self.save_button = tk.Button(self.dialog, text='Save', command=self.save_task)
        self.save_button.grid(row=4, column=0, columnspan=2, pady=10)

        if self.task:
            self.delete_button = tk.Button(self.dialog, text='Delete', command=self.delete_task)
            self.delete_button.grid(row=4, column=2, columnspan=2, pady=10)

    def toggle_deadline(self):
        state = tk.DISABLED if self.deadline_var.get() else tk.NORMAL
        self.deadline_entry.config(state=state)
        self.hour_spinbox.config(state=state)
        self.minute_spinbox.config(state=state)

    def save_task(self):
        title = self.title_entry.get()
        description = self.description_text.get("1.0", tk.END).strip()
        deadline = None
        if not self.deadline_var.get():
            date = self.deadline_entry.get_date()
            hour = int(self.hour_spinbox.get())
            minute = int(self.minute_spinbox.get())
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
        if self.task:
            self.task_list.tasks.remove(self.task)
            self.callback()
            self.dialog.destroy()
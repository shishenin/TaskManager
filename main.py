import tkinter as tk
from task_manager.app import TaskManagerApp

def main():
    """
    Основная точка входа в приложение Task Manager.
    Создаёт главное окно tkinter и запускает приложение.
    """
    root = tk.Tk()
    TaskManagerApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
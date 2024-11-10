# main.py

import tkinter as tk
from task_manager.app import TaskManagerApp

def main():
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()

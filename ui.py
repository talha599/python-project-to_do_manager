import customtkinter as ctk
from datetime import datetime
from models import Task
from manager import TaskManager


class App(ctk.CTk):
    """
    Main UI Controller.
    """

    def __init__(self):
        super().__init__()

        self.title("To-Do Manager")
        self.geometry("700x500")

        self.manager = TaskManager()

        self.create_widgets()
        self.refresh_tasks()

    def create_widgets(self):

        self.title_label = ctk.CTkLabel(self, text="Task Dashboard", font=("Arial", 24))
        self.title_label.pack(pady=10)

        self.search_entry = ctk.CTkEntry(self, placeholder_text="Search task...")
        self.search_entry.pack(pady=5)

        ctk.CTkButton(self, text="Search", command=self.search_task).pack(pady=5)

        ctk.CTkButton(self, text="Sort by Priority", command=self.sort_tasks).pack(pady=5)

        self.task_frame = ctk.CTkFrame(self)
        self.task_frame.pack(fill="both", expand=True, padx=10, pady=10)

        ctk.CTkButton(self, text="Add Task", command=self.open_add_window).pack(pady=5)
        ctk.CTkButton(self, text="Show Report", command=self.show_report).pack(pady=5)

    def refresh_tasks(self):

        for widget in self.task_frame.winfo_children():
            widget.destroy()

        for i, task in enumerate(self.manager.tasks):

            text = f"{task.title} | {task.priority} | Due: {task.due_date}"
            if task.completed:
                text += " ✔"

            label = ctk.CTkLabel(self.task_frame, text=text)
            label.grid(row=i, column=0, padx=5, pady=5)

            ctk.CTkButton(
                self.task_frame,
                text="Done",
                width=60,
                command=lambda i=i: self.complete_task(i)
            ).grid(row=i, column=1)

            ctk.CTkButton(
                self.task_frame,
                text="Delete",
                width=60,
                command=lambda i=i: self.delete_task(i)
            ).grid(row=i, column=2)

    def complete_task(self, index):
        self.manager.toggle_complete(index)
        self.refresh_tasks()

    def delete_task(self, index):
        self.manager.delete_task(index)
        self.refresh_tasks()

    def search_task(self):
        keyword = self.search_entry.get()
        results = self.manager.search(keyword)

        for widget in self.task_frame.winfo_children():
            widget.destroy()

        for task in results:
            text = f"{task.title} | {task.priority} | Due: {task.due_date}"
            ctk.CTkLabel(self.task_frame, text=text).pack()

    def sort_tasks(self):
        self.manager.sort_by_priority()
        self.refresh_tasks()

    def open_add_window(self):

        win = ctk.CTkToplevel(self)
        win.title("Add Task")
        win.geometry("350x250")

        title = ctk.CTkEntry(win, placeholder_text="Task Title")
        title.pack(pady=5)

        priority = ctk.CTkOptionMenu(win, values=["Low", "Medium", "High"])
        priority.pack(pady=5)

        due = ctk.CTkEntry(win, placeholder_text="YYYY-MM-DD")
        due.pack(pady=5)

        def save_task():
            t = title.get()
            p = priority.get()
            d = due.get()

            if not t or not d:
                return

            try:
                datetime.strptime(d, "%Y-%m-%d")
            except ValueError:
                return

            task = Task(t, p, d)
            self.manager.add_task(task)

            win.destroy()
            self.refresh_tasks()

        ctk.CTkButton(win, text="Save", command=save_task).pack(pady=10)

    def show_report(self):

        total, completed, pending = self.manager.get_report()

        win = ctk.CTkToplevel(self)
        win.title("Report")
        win.geometry("350x250")

        report_text = f"""
Total Tasks: {total}
Completed: {completed}
Pending: {pending}
"""

        ctk.CTkLabel(win, text=report_text).pack(pady=20)

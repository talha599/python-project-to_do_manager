from models import Task
from storage import JsonStorage
 
 
class TaskManager:
    """
    Handles business logic (CRUD, search, report).
    """
 
    def __init__(self):
        self.storage = JsonStorage()
        self.tasks = [Task.from_dict(t) for t in self.storage.load()]
 
    def save(self):
        self.storage.save([t.to_dict() for t in self.tasks])




# -------- CRUD --------
 
    def add_task(self, task):
        self.tasks.append(task)
        self.save()
 
    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save()
 
    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = new_task
            self.save()
 
    def toggle_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = not self.tasks[index].completed
            self.save()



    # -------- Search --------
 
    def search(self, keyword):
        return [
            task for task in self.tasks
            if keyword.lower() in task.title.lower()
        ]

 
 
    # -------- Sort --------
 
    def sort_by_priority(self):
        priority_order = {"High": 1, "Medium": 2, "Low": 3}
        self.tasks.sort(key=lambda t: priority_order[t.priority])

 
 
    # -------- Report --------
 
    def get_report(self):
        total = len(self.tasks)
        completed = len([t for t in self.tasks if t.completed])
        pending = total - completed
        return total, completed, pending

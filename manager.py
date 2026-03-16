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

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
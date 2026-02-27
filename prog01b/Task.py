import uuid

class Task:
    def __init__(self, description, status='Pending'):
        self.task_id = str(uuid.uuid4())
        self.description = description
        self.status = status

    def getId(self):
        return self.task_id
    
    def getDescription(self):
        return self.description

    def getStatus(self):
        return self.status
    
    def setStatus(self, status):
        self.status = status
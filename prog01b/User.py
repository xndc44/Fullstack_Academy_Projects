from prog01b.Task import Task

class User:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.tasks = {}
    
    def getPass(self):
        return self.password
    
    def mark_as_complete(self):
        self.getTasks()
        if self.tasks:
            task_id = input('Enter task id to mark as complete: ')
            task = self.tasks[task_id]
            task.setStatus('Completed')
            print('Task completed.')
        else: print('No tasks to complete')

    def addTask(self, task_id, task: Task):
        self.tasks[task_id] = task

    def delete_task(self, task_id):
        if not self.tasks:
            print('No tasks to delete')
            return
        del self.tasks[task_id]

    def view_tasks(self):
        for t in self.tasks.values():
            print(f'Task ID: {t.getId()}\nDescription: {t.getDescription()}\nStatus: {t.getStatus()}')

    def getTasks(self):
        # Each task should show the task ID, description, and status (Pending or Completed)
        return self.tasks
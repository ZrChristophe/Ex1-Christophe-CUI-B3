# Controllers/task_controller.py

from model.task import Task, TimedTask

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            raise TaskNotFoundError()

    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].done = True
        else:
            raise TaskNotFoundError()

    def list_tasks(self):
        return self.tasks

class TaskNotFoundError(Exception):
    pass

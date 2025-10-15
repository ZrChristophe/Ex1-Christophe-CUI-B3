from datetime import datetime

class Task:
    def __init__(self, title: str, description: str = ""):
        self.title = title
        self.description = description
        self.done = False

    def mark_done(self):
        self.done = True

    def __str__(self):
        status = "✔" if self.done else "✘"
        return f"[{status}] {self.title} - {self.description}"

class TimedTask(Task):
    def __init__(self, title: str, description: str = "", due_date: str = None):
        super().__init__(title, description)
        self.due_date = due_date  # format "YYYY-MM-DD"

    def __str__(self):
        base = super().__str__()
        return f"{base} (Échéance: {self.due_date})"
#
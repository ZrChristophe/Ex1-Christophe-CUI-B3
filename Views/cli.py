# Views/cli.py
from controllers.task_controller import TaskManager, TaskNotFoundError
from model.task import Task, TimedTask

class CLI:
    def __init__(self):
        self.controller = TaskManager()  # On utilise la classe existante TaskManager

    def show_menu(self):
        print("\n=== ToDoList CLI ===")
        print("1. Ajouter une tâche")
        print("2. Supprimer une tâche")
        print("3. Afficher toutes les tâches")
        print("4. Quitter")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Choisissez une option : ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.delete_task()
            elif choice == "3":
                self.mark_task_done()
            elif choice == "4":
                print("Au revoir !")
                break
            else:
                print("Option invalide, réessayez.")

    def add_task(self):
        title = input("Titre de la tâche : ")
        description = input("Description (optionnelle) : ")
        due_date = input("Échéance (YYYY-MM-DD, optionnelle) : ")
        if due_date:
            task = TimedTask(title, description, due_date)
        else:
            task = Task(title, description)
        self.controller.add_task(task)
        print("Tâche ajoutée !")

    def delete_task(self):
        self.show_tasks()
        try:
            index = int(input("Numéro de la tâche à supprimer : ")) - 1
            self.controller.delete_task(index)
            print("Tâche supprimée !")
        except (ValueError, TaskNotFoundError):
            print("Erreur : tâche non trouvée.")

    def show_tasks(self):
        tasks = self.controller.list_tasks()
        if not tasks:
            print("Aucune tâche.")
        else:
            for i, task in enumerate(tasks, 1):
                status = "✓" if getattr(task, "done", False) else "✗"
                print(f"{i}. [{status}] {task}")

    def mark_task_done(self):
        self.show_tasks()
        try:
            index = int(input("Numéro de la tâche à marquer comme faite : ")) - 1
            self.controller.mark_done(index)
            print("Tâche marquée comme faite !")
        except (ValueError, TaskNotFoundError):
            print("Erreur : tâche non trouvée.")


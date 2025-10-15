from flask import Flask, render_template, request, redirect, url_for
from controllers.task_controller import TaskController

app = Flask(__name__)
controller = TaskController()

@app.route('/')
def index():
    tasks = controller.get_all_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description', "")
    due_date = request.form.get('due_date', None)
    controller.add_task(title, description, due_date)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_task(index):
    controller.delete_task(index)
    return redirect(url_for('index'))

@app.route('/done/<int:index>')
def mark_done(index):
    controller.mark_task_done(index)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)

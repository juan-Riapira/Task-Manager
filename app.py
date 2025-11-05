from flask import Flask, redirect, url_for
from app.routes.tasks_routes import task_bp


app = Flask(__name__)

app.register_blueprint(task_bp, url_prefix='/tasks')

@app.route('/')
def home():
    return redirect(url_for('tasks.list_tasks'))

if __name__ == '__main__':
    app.run(debug=True)

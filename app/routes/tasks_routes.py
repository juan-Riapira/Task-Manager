from flask import Blueprint, request, jsonify, render_template
from app.services.task_service import load_tasks, add_task, update_task, delete_task, save_tasks


task_bp = Blueprint('tasks', __name__)

# ------------------------------
# CRUD task routes
# ------------------------------

@task_bp.route('/', methods=['GET'])
def list_tasks():
    """
    Retrieve and display all tasks.

    This route loads all existing tasks and renders them in the main page template (`index.html`).

    Returns:
        HTML: Rendered template with the list of tasks.
    """
    tasks = load_tasks()
    return render_template('index.html', tasks=tasks)


@task_bp.route('/', methods=['POST'])
def create_task():
    """
    Create a new task.

    This route receives a JSON payload containing task data (at least a 'title'),
    adds the new task, and returns it as JSON.

    Expected JSON body:
        {
            "title": "Task title",
            "description": "Optional task description"
        }

    Returns:
        JSON: The created task object with a 201 status code.
        400: If required data is missing.
    """
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Missing title'}), 400

    task = add_task(data)
    return jsonify(task), 201


@task_bp.route('/<int:task_id>', methods=['PUT'])
def modify_task(task_id):
    """
    Update an existing task.

    This route updates the task identified by its ID with new data
    sent in the request body.

    Args:
        task_id (int): The ID of the task to be updated.

    Expected JSON body:
        {
            "title": "Updated title",
            "description": "Updated description",
            "completed": true
        }

    Returns:
        JSON: The updated task object.
        404: If the task does not exist.
    """
    data = request.get_json()
    task = update_task(task_id, data)
    if task:
        return jsonify(task)
    return jsonify({"error": "Task not found"}), 404


@task_bp.route('/<int:task_id>', methods=['DELETE'])
def remove_task(task_id):
    """
    Delete a task by its ID.

    Args:
        task_id (int): The ID of the task to delete.

    Returns:
        JSON: Confirmation message with status 200.
    """
    delete_task(task_id)
    return jsonify({"message": "Deleted successfully"}), 200

# ------------------------------
# TASK BOARD FUNCTIONALITY

@task_bp.route('/board', methods=['GET'])
def board():
    """
    Display the task board grouped by status.

    Tasks are grouped into three categories:
        - "Por hacer" (To Do)
        - "Haciendo" (In Progress)
        - "Hecho" (Done)

    Returns:
        HTML: Rendered template (`board.html`) displaying tasks grouped by status.
    """
    tasks = load_tasks()
    grouped = {
        "To Do": [t for t in tasks if t.get("status") == "To Do"],
        "Doing": [t for t in tasks if t.get("status") == "Doing"],
        "Done": [t for t in tasks if t.get("status") == "Done"]
    }
    return render_template('board.html', tasks_grouped=grouped)


@task_bp.route('/update_status/<int:task_id>', methods=['PUT'])
def update_status(task_id):
    """
    Update the status of a specific task.

    Args:
        task_id (int): The ID of the task whose status will be updated.

    Expected JSON body:
        {
            "status": "To Do" | "Doing" | "Done"
        }

    Returns:
        JSON: Updated task object with status 200.
        400: If 'status' is missing from the request.
        404: If the task does not exist.
    """
    data = request.get_json()
    if not data or "status" not in data:
        return jsonify({"error": "Missing status"}), 400

    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["status"] = data["status"]
            save_tasks(tasks)
            return jsonify(t), 200

    return jsonify({"error": "Task not found"}), 404

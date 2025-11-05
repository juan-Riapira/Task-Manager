import json
import os
from typing import List, Dict, Optional


DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'tasks.json')


def load_tasks() -> List[Dict]:
    """
    Load all tasks from the JSON file.

    Returns:
        list: A list of dictionaries representing the tasks.
              Returns an empty list if the file does not exist or cannot be parsed.
    """
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, 'r', encoding='utf-8') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_tasks(tasks: List[Dict]) :
    """
    Save the list of tasks to the JSON file.

    Args:
        tasks (list): A list of dictionaries containing task data.
    """
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)


def add_task(data: Dict) :
    """
    Add a new task to the JSON data file.

    Args:
        data (dict): A dictionary containing the new task's data.
                     Example: {"title": "Study Flask", "description": "Review routes and templates"}
|
    Returns:
        dict: The newly created task with an assigned ID.
    """
    tasks = load_tasks()
    new_id = max([t.get('id', 0) for t in tasks], default=0) + 1
    data['id'] = new_id
    data.setdefault('status', 'To Do')

    tasks.append(data)
    save_tasks(tasks)
    return data


def update_task(task_id: int, new_data: Dict) :
    """
    Update an existing task based on its ID.

    Args:
        task_id (int): The ID of the task to update.
        new_data (dict): A dictionary with the new task data.

    Returns:
        dict | None: The updated task if found, otherwise None.
    """
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task.update(new_data)
            save_tasks(tasks)
            return task
    return None


def delete_task(task_id: int) :
    """
    Delete a task by its ID.

    Args:
        task_id (int): The ID of the task to delete.

    Returns:
        bool: True if deletion was successful.
    """
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(updated_tasks)
    return True

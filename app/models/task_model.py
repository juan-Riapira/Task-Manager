class Task:
    """
    Represents a task with an ID, title, description, and completion status.

    Attributes:
        id (int): The unique identifier of the task.
        title (str): The title or name of the task.
        description (str): A detailed explanation of the task.
        completed (bool): Indicates whether the task is completed (default is False).
    """

    def __init__(self, id, title, description, completed=False):
        """
        Initializes a new Task instance.

        Args:
            id (int): The unique identifier for the task.
            title (str): The title of the task.
            description (str): The description of the task.
            completed (bool, optional): The task’s completion status. Defaults to False.
        """
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    def to_dict(self):
        """
        Converts the Task object into a dictionary representation.

        Returns:
            dict: A dictionary containing task data with keys:
                - "id": int
                - "title": str
                - "description": str
                - "completed": bool
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }

// Save or update task
document.getElementById("taskForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const id = document.getElementById("taskId").value;
    const title = document.getElementById("title").value.trim();
    const description = document.getElementById("description").value.trim();
    const status = document.getElementById("status").value;

    if (!title) {
        alert("Title is required.");
        return;
    }

    const task = { title, description, status };
    const method = id ? "PUT" : "POST";
    const url = id ? `/tasks/${id}` : "/tasks/";

    const response = await fetch(url, {
        method,
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(task),
    });

    if (response.ok) {
        location.reload();
    } else {
        alert("Error saving the task.");
    }
});

// Load data for editing
document.querySelectorAll(".edit-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
        document.getElementById("taskId").value = btn.dataset.id;
        document.getElementById("title").value = btn.dataset.title;
        document.getElementById("description").value = btn.dataset.description;
        document.getElementById("status").value = btn.dataset.status;
    });
});

// Delete task
document.querySelectorAll(".delete-btn").forEach((btn) => {
    btn.addEventListener("click", async () => {
        if (!confirm("Delete task?")) return;

        const id = btn.dataset.id;
        const response = await fetch(`/tasks/${id}`, { method: "DELETE" });

        if (response.ok) {
            location.reload();
        } else {
            alert("Error deleting the task.");
        }
    });
});

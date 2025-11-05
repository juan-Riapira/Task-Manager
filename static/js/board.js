// --- Board Drag & Drop ---
function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("id", ev.target.dataset.id);
}

function drop(ev, newStatus) {
    ev.preventDefault();
    const id = ev.dataTransfer.getData("id");

    fetch(`/tasks/update_status/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ status: newStatus })
    })
    .then((res) => {
        if (res.ok) {
            location.reload();
        } else {
            alert("Error updating task status.");
        }
    })
    .catch(() => alert("Server connection error."));
}

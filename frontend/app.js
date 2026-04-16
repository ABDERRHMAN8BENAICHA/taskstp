const API = "https://tasks-api-t76h.onrender.com";

// Helper validation
function isEmpty(value) {
    return !value || value.trim() === "";
}

function isValidEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

//  Register
async function register() {
    const username = document.getElementById("username").value;
    const email = document.getElementById("reg_email").value;
    const password = document.getElementById("reg_password").value;

    // Validation
    if (isEmpty(username) || isEmpty(email) || isEmpty(password)) {
        alert("All fields are required");
        return;
    }

    if (!isValidEmail(email)) {
        alert("Invalid email format");
        return;
    }

    if (password.length < 6) {
        alert("Password must be at least 6 characters");
        return;
    }

    try {
        const res = await fetch(API + "/auth/register", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({ username, email, password })
        });

        const data = await res.json();

        if (!res.ok) {
            alert(data.detail || "Registration failed");
            return;
        }

        alert(" Registered successfully!");
    } catch (err) {
        alert("Server error");
    }
}


//  Login
async function login() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    // Validation
    if (isEmpty(email) || isEmpty(password)) {
        alert("Email and password are required");
        return;
    }

    if (!isValidEmail(email)) {
        alert("Invalid email format");
        return;
    }

    try {
        const res = await fetch(API + "/auth/login", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({ email, password })
        });

        const data = await res.json();

        if (!res.ok) {
            alert(data.detail || "Login failed");
            return;
        }

        localStorage.setItem("user_id", data.id);
        window.location.href = "dashboard.html";

    } catch (err) {
        alert("Server error");
    }
}


//  Logout
function logout() {
    localStorage.removeItem("user_id");
    window.location.href = "index.html";
}


//  Add Task
async function addTask() {
    const title = document.getElementById("title").value;
    const description = document.getElementById("desc").value;
    const user_id = localStorage.getItem("user_id");

    // Validation
    if (isEmpty(title) || isEmpty(description)) {
        alert("Title and description are required");
        return;
    }

    if (!user_id) {
        alert("You must login first");
        return;
    }

    try {
        const res = await fetch(API + "/tasks/tasks", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({ title, description, user_id })
        });

        if (!res.ok) {
            alert("Failed to add task");
            return;
        }

        document.getElementById("title").value = "";
        document.getElementById("desc").value = "";

        loadTasks();

    } catch (err) {
        alert("Server error");
    }
}


//  Load Tasks
async function loadTasks() {
    const user_id = localStorage.getItem("user_id");

    if (!user_id) {
        alert("Not logged in");
        return;
    }

    try {
        const res = await fetch(API + `/tasks/tasks/${user_id}`);
        const tasks = await res.json();

        const list = document.getElementById("tasks");
        list.innerHTML = "";

        tasks.forEach(t => {
            const li = document.createElement("li");
            li.innerHTML = `
                ${t.title} - ${t.description}
                <button onclick="deleteTask('${t._id}')">Delete</button>
            `;
            list.appendChild(li);
        });

    } catch (err) {
        alert("Failed to load tasks");
    }
}


//  Delete Task
async function deleteTask(id) {
    if (!id) return;

    try {
        await fetch(API + `/tasks/tasks/${id}`, {
            method: "DELETE"
        });

        loadTasks();

    } catch (err) {
        alert("Delete failed");
    }
}
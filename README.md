# 📝 To-Do Manager (with Priority Python Desktop GUI)

### 📌 Overview

The **To-Do Manager with Priority** is a desktop-based task management application developed using Python and the `customtkinter` GUI library. The application allows users to efficiently organize, track, and manage daily tasks with priority levels and due dates.

This project is designed using proper **Object-Oriented Programming (OOP)** principles and follows a modular architecture where each component (model, manager, storage, and UI controller) is separated into different files for maintainability and scalability.

The system ensures data persistence using a JSON file, meaning all tasks remain saved even after restarting the application.

---

### 🎯 Objective

The main objective of this project is to:

* Develop a structured desktop application using Python.
* Implement CRUD operations with proper validation.
* Apply OOP concepts in a real-world system.
* Store and retrieve data using JSON.
* Provide task tracking with summary reporting.


---

# 📌 Features

### ✅ Core Features

* Add Task
* Delete Task
* Mark Task as Completed
* View Task List

### 🔍 Search & Sort

* Search tasks by title
* Sort tasks by priority (High → Low)

### 📊 Reports

* Total Tasks
* Completed Tasks
* Pending Tasks

### 💾 Data Persistence

* Tasks are saved in `data.json`
* Data remains after restarting the app

### 🛡 Validation

* Prevent empty fields
* Validate date format (YYYY-MM-DD)
* No crashes on invalid input

---

# 🏗️ Project Structure

```
todo_manager/
│
├── main.py          # Entry point
├── ui.py            # GUI (Controller)
├── manager.py       # Business logic
├── models.py        # Task entity
├── storage.py       # JSON storage handler
├── data.json        # Data file (auto-created)
└── requirements.txt # Dependencies
```


# ⚙️ Setup Instructions

## 1️⃣ Clone or Download Project

Download the project folder or clone from Git:

```
git clone (https://github.com/talha599/python-project-to_do_manager)
code .
```

---

## 2️⃣ Create Virtual Environment

```
python -m venv .venv
```

---

## 3️⃣ Activate Environment

### Windows:

```
.venv\Scripts\activate
```

### macOS/Linux:

```
source .venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```
pip install -r requirements.txt
```

If `requirements.txt` is missing:

```
pip install customtkinter
pip freeze > requirements.txt
```

---

## ▶️ Run the Application

```
python main.py
```

---

# 📸 Screenshots of To-Do Manager: 
1.	Dashboard (Task List)
 
<img width="779" height="592" alt="image" src="https://github.com/user-attachments/assets/b21fd950-0531-4d30-b574-4f256ce4c7f0" />

2.	Add Task Window
 
<img width="666" height="537" alt="image" src="https://github.com/user-attachments/assets/b6397d4b-e44a-4524-9f3c-20b2dc38805f" />

3.	Search Result
 
<img width="851" height="400" alt="image" src="https://github.com/user-attachments/assets/20127140-788d-467d-9b09-92c9d6ae7f9d" />


4.	Sort Window
 
<img width="851" height="400" alt="image" src="https://github.com/user-attachments/assets/bdd2ba86-da23-44ef-8d7b-5ab84e56bb4e" />


5.	Report Window
 
<img width="774" height="381" alt="image" src="https://github.com/user-attachments/assets/489c31b5-faa3-49cb-9b8d-4dbfa0ef7027" />


6.	Completed Task View
   
 <img width="802" height="500" alt="image" src="https://github.com/user-attachments/assets/b652f7e4-927d-4ffc-909b-1e6c91325d25" />

---

# 📊 Sample Data (data.json)

```
[
  {
    "title": "Finish Assignment",
    "priority": "High",
    "due_date": "2026-03-28",
    "completed": false
  }
]
```



# ⚠️ Notes

* The app automatically creates `data.json` on first run
* Make sure Python is installed (version 3.8+ recommended)
* Always activate `.venv` before running the project

---

# 🚀 Future Improvements (Optional)

* Edit Task feature
* Filter by status (Completed/Pending)
* Due date reminders
* Export tasks to CSV
* Dark/Light mode toggle

---

# 👨‍💻 Author 1

Name: Muhammad Talha Islam
Email: 22-49599-3@student.aiub.edu
---


# 👨‍💻 Author 2

Name: Wafa
Email: 22-49542-3@student.aiub.edu
---

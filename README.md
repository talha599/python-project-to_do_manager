# 📝 To-Do Manager (with Priority Python Desktop GUI)

A modern **Python Desktop GUI application** to manage daily tasks with priority, due dates, search, and productivity reports.
Built using **customtkinter**.

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
 





2.	Add Task Window
 


3.	Search Result
 



4.	Sort Window
 



5.	Report Window
 






6.	Completed Task View
 


---

# 📊 Sample Data (data.json)

```
[
  {
    "title": "Finish Assignment",
    "priority": "High",
    "due_date": "2026-03-20",
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

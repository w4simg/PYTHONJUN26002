# Django Server and Database Management Guide

This guide explains how to run your Django development server and check your SQLite database contents.

---

## 1. How to Run the Django Server

To start the local development server, follow these steps:

1. Open your terminal/command prompt.
2. Navigate (`cd`) to the directory containing your project's `manage.py` file:
   ```bash
   cd Month-1/Week-3/Day-3/Assignments/StudentProject
   ```
3. Run the Django development server:
   ```bash
   python manage.py runserver
   ```
4. By default, the server starts at **`http://127.0.0.1:8000/`**.
5. You can test your APIs using Postman or a browser by visiting:
   - **GET API**: `http://127.0.0.1:8000/api/students/`
   - **POST API**: Send JSON payloads (e.g. `{"name": "Alice", "email": "alice@example.com", "phone": "1234567890", "course": "Django"}`) to `http://127.0.0.1:8000/api/students/`

*Note: To stop the server at any time, press `Ctrl + C` in the terminal.*

---

## 2. How to Check the Database

Since Django uses SQLite (`db.sqlite3`) by default, you can view and query database records in three ways:

### Option A: Using Django Admin Panel (Most User-Friendly)
The Django Admin interface provides a full GUI to create, read, update, and delete student records.

1. **Create a superuser account**:
   Run this command in the terminal and follow the prompts to enter a username, email, and password:
   ```bash
   python manage.py createsuperuser
   ```
2. **Start the server** (if not already running):
   ```bash
   python manage.py runserver
   ```
3. **Login to Admin Panel**:
   Open your browser and navigate to: `http://127.0.0.1:8000/admin/`
4. Log in using the superuser credentials you created. You will see **Students** under the **StudentApp** section. Click on it to browse, add, edit, or delete records.

---

### Option B: Using the Django Python Shell
You can query records directly using Django's interactive shell.

1. **Start the shell**:
   ```bash
   python manage.py shell
   ```
2. **Import the Student model and run queries**:
   ```python
   from StudentApp.models import Student

   # Get all student records
   students = Student.objects.all()
   print(students)

   # Loop and print details
   for s in students:
       print(s.id, s.name, s.email, s.course)
   ```
3. Exit the shell by typing `exit()`.

---

### Option C: Using SQLite Viewer in VS Code or DB Browser
Since `db.sqlite3` is a file, you can inspect it directly using third-party database viewer tools:

1. **VS Code Extension (Recommended)**:
   - Install the extension **"SQLite Viewer"** in VS Code.
   - Simply click on the `db.sqlite3` file inside your project file explorer to browse all tables (e.g. `StudentApp_student`) and records in a interactive grid.
2. **DB Browser for SQLite (Desktop App)**:
   - Download and install [DB Browser for SQLite](https://sqlitebrowser.org/).
   - Open the app, click **Open Database**, and select the `db.sqlite3` file. Go to the "Browse Data" tab to view your tables.

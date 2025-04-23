# 📝 Django Task Management App

This is a full-featured task management system built using Django. It includes user registration and login, profile management, security settings, and task operations categorized by status and type.

---

## 🚀 Features

- User registration with validation
- Login using username or email
- Profile management (with editable fields)
- Task creation, update, deletion
- Filter tasks by category and status
- Security settings (email & password update)
- Simple UI integration with Django templates
- Built-in session handling using Django's `@login_required` decorators

---

## 🛠️ Tech Stack

- **Backend**: Django
- **Database**: SQLite (default Django)
- **Frontend**: HTML/CSS (Django templating)
- **Authentication**: Django's `auth` system

---

## 📁 Project Structure

project/ │ ├── app/ │ ├── views.py │ ├── urls.py │ ├── models.py │ └── templates/ │ ├── authentication/ │ │ ├── login.html │ │ └── register.html │ ├── index.html │ ├── profile.html │ ├── profile_modal.html │ ├── security_modal.html │ ├── task.html │ ├── task_category.html │ └── task_status.html │ ├── manage.py └── README.md


---

## 🔐 User Authentication Routes

| URL | View Function | Description |
|-----|----------------|-------------|
| `/register/` | `register` | User signup (Note: Plain-text password, insecure for production) |
| `/login/` | `user_login` | Login using username or email |
| `/logout/` | `user_logout` | Logout the current user |

---

## 👤 Profile & Security Routes

| URL | View Function | Description |
|-----|----------------|-------------|
| `/profile/` | `profile` | Show and edit user profile |
| `/load_profile_content/` | `load_profile_content` | Loads profile content via AJAX |
| `/update_profile/` | `update_profile` | Updates profile fields |
| `/load_security_content/` | `load_security_content` | Loads email/password change form |
| `/update_security/` | `update_security` | Updates user's email and password |

---

## ✅ Task Management Routes

| URL | View Function | Description |
|-----|----------------|-------------|
| `/tasks/` | `task_management` | Shows all tasks created by the user |
| `/tasks/add/` | `add_task` | Add a new task |
| `/tasks/edit/<int:task_id>/` | `edit_task` | Edit an existing task |
| `/tasks/delete/<int:task_id>/` | `delete_task` | Delete a task |
| `/tasks/load/<str:category>/` | `load_tasks_by_category` | Filter tasks by category |
| `/tasks/status/<str:status>/` | `load_tasks_by_status` | Filter tasks by status |

---

## ⚠️ Important Notes

- ❌ Passwords are stored as **plain text**, which is highly insecure.
  - ✅ **Use `set_password()` and `check_password()`** methods from Django for real applications.
- ❌ No CSRF protection for some `POST` routes like `add_task`, `edit_task`.
  - ✅ Include `{% csrf_token %}` in forms and ensure proper decorators.

---

## 💡 Setup Instructions

```bash
# Clone the repository
git clone <repo-url>

# Navigate into the project directory
cd project

# Create and activate a virtual environment (optional)
python -m venv env
source env/bin/activate  # For Linux/macOS
env\Scripts\activate     # For Windows

# Install dependencies
pip install django

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver

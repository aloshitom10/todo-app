# Todo App

A Django-based todo application for adding, viewing, updating, and deleting tasks. Each task includes a task name and date, making it useful for tracking simple daily work or reminders.

## Features

- Add new tasks
- View all tasks on the home page
- Update existing tasks
- Delete completed or unwanted tasks
- Store task names and dates
- SQLite database for local development
- Template-based HTML interface
- Custom CSS styling

## Tech Stack

- Python
- Django
- SQLite
- HTML
- CSS

## Project Structure

```text
myproject/
|-- myapp/             # Main todo application
|-- myproject/         # Django project settings
|-- db.sqlite3         # SQLite database
`-- manage.py          # Django management script
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/aloshitom10/todo-app.git
cd todo-app
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install Django:

```bash
pip install django
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Run the development server:

```bash
python manage.py runserver
```

6. Open the app in your browser:

```text
http://127.0.0.1:8000/
```

## Usage

Open the home page to add a task with a name and date. Existing tasks can be edited or deleted directly from the task list.

## Repository Topics

```text
django todo-app crud python sqlite
```

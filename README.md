Django Tutorials
================

This repository contains two Django projects:

1. **djangocourse** (root project): web pages, products, comments, and REST API endpoints for products/comments.
2. **todoapp** (subfolder project): Todo REST API with token authentication (signup/login) and CRUD operations.

Requirements
------------

- Python 3.14+
- Django 6.0.2
- Django REST Framework

Setup
-----

1. Clone the repository:

```bash
git clone https://github.com/EmiltonMenaA/called-DjangoTutorials.git
cd called-DjangoTutorials
```

2. Create and activate virtual environment (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install django==6.0.2 djangorestframework factory-boy
```

Project 1: djangocourse (root)
------------------------------

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Optional seed command:

```bash
python manage.py seed_products
```

Run server:

```bash
python manage.py runserver --settings=djangocourse.settings
```

Main API endpoints:

- `GET/POST /api/products/`
- `GET/PUT/PATCH/DELETE /api/products/<id>/`
- `GET/POST /api/comments/`
- `GET/PUT/PATCH/DELETE /api/comments/<id>/`

Project 2: todoapp
------------------

Move into project:

```bash
cd todoapp
```

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Run server:

```bash
python manage.py runserver
```

Auth endpoints:

- `POST /api/signup/`
- `POST /api/login/`

Todo endpoints (token required):

- `GET/POST /api/todos/`
- `GET/PUT/PATCH/DELETE /api/todos/<id>/`
- `PUT/PATCH /api/todos/<id>/complete`

Notes
-----

- If you get 404 at `/`, use API routes directly.
- Use only one Django server at a time on port `8000` to avoid confusion between projects.

Author
------

Emilton Mena Acevedo


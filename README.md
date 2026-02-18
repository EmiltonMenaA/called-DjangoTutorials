Django Tutorials — Online Store
===============================

A comprehensive Django application showcasing a complete e-commerce system with products, comments, factory-based data seeding, and professional code quality standards.

## Features

- **Product Management**: Create, list, and view products with detailed information
- **Comments System**: Add and display comments linked to products via ForeignKey relationships
- **Factory Boy Integration**: Automated database seeding with realistic test data
- **Database Management**: SQLite database with factory-based product generation
- **Professional Code Quality**: Black, isort, flake8, and autopep8 integrated
- **Responsive Templates**: Bootstrap-based UI with static styling
- **Management Commands**: Custom Django commands for database operations

## Project Structure

```
.
├── djangocourse/          # Main Django project settings
├── pages/                 # Main app
│   ├── models.py         # Product & Comment models
│   ├── views.py          # View controllers
│   ├── factories.py       # Factory Boy factories for testing
│   ├── urls.py           # URL routing
│   ├── admin.py          # Django admin configuration
│   ├── management/
│   │   └── commands/
│   │       └── seed_products.py  # Database seeding command
│   ├── static/
│   │   └── pages/
│   │       └── app.css           # Custom styling
│   └── templates/
│       └── products/             # Product templates
├── manage.py             # Django management script
├── db.sqlite3            # SQLite database
└── README.md
```

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/EmiltonMenaA/called-DjangoTutorials.git
cd called-DjangoTutorials
```

### 2. Create and activate virtual environment (Windows PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Or manually install:
```bash
pip install django==6.0.2
pip install factory-boy
pip install black isort flake8 autopep8
pip install sqlite-web
```

### 4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Seed the database with sample data

```bash
python manage.py seed_products
```

This creates 8 products with randomly generated names and prices.

### 6. Run the development server

```bash
python manage.py runserver
```

Access the application at **http://127.0.0.1:8000/**

## Routes

| Route | Description |
|-------|-------------|
| `/` | Home page |
| `/about/` | About page |
| `/contact/` | Contact page |
| `/products/` | Product listing |
| `/products/<id>` | Product detail with comments |
| `/products/create` | Create new product form |

## Database Models

### Product Model
```python
class Product(models.Model):
    name = CharField(max_length=255)
    price = IntegerField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
```

### Comment Model
```python
class Comment(models.Model):
    product = ForeignKey(Product, on_delete=models.CASCADE)
    description = TextField()
```

## Code Quality Tools

This project uses professional Python linting and formatting:

- **Black**: Code formatter
- **isort**: Import sorting
- **flake8**: Style guide enforcement
- **autopep8**: Automatic PEP 8 compliance

Run code quality checks:
```bash
black pages/ djangocourse/
isort pages/ djangocourse/
flake8 pages/ djangocourse/
```

## Database Viewer

To view your SQLite database visually:

```bash
pip install sqlite-web
sqlite_web db.sqlite3
```

Open **http://localhost:8080** in your browser

## Technologies Used

- **Django 6.0.2** - Web framework
- **SQLite** - Database
- **Factory Boy** - Test data generation
- **Bootstrap 5** - Frontend framework
- **Black** - Code formatting
- **flake8** - Code linting

## Notes

- This is an educational project demonstrating Django best practices
- All products and comments are stored in SQLite database
- The application includes management commands for database operations
- Code follows PEP 8 standards with professional formatting

## Author

Developed by: **Emilton Mena Acevedo**


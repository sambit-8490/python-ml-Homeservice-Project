# HomeServiceManagement

HomeServiceManagement is a **Django-based web application** for managing home services, service providers, customers, and orders. It supports user registration, login, admin management, and service bookings.

---

## Features

### User Features
- User signup and login (as Customer or Service Man)
- View and edit profile
- Browse available services
- Book services and view orders
- Search services by category or city
- Contact form for inquiries

### Admin Features
- Admin login
- Dashboard showing counts of Customers, Services, and Service Men
- Manage Services, Service Categories, and Cities
- Approve or change status of Service Men and Orders
- View and mark customer messages as read
- Admin profile management and password change

---

## Project Structure
HomeServiceManagement/
├── home_service/ # Main Django app
├── media/ # Uploaded images
├── venv/ # Python virtual environment
├── db.sqlite3 # SQLite database
├── manage.py # Django management script
├── requirements.txt # Python dependencies
└── Dockerfile # Docker configuration


---

## Prerequisites

- Python 3.10+
- Django 4.x+
- Docker (optional, for containerized deployment)

---

## Setup Instructions (Without Docker)

1. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
Run database migrations:
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000


Setup Instructions (Using Docker)

Build the Docker image:

docker build -t homeservice-app .

Run the container:

docker run -p 8000:8000 homeservice-app

Create superuser inside container:

docker exec -it blissful_blackburn (container name) /bin/sh

python manage.py createsuperuser

Example input for superuser creation:

Username: admin@123
Email address: admin@gmail.com
Password: admin@123
Password (again): admin@123

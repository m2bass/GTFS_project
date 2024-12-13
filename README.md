# Rideshare Application

A Django-based web application for managing rideshare trips and stops. The app allows users to create, update, and view trip information, including associated stops, with validation checks for duplicate stop IDs.

## Features

- **Trip Management**: Create and update trips with details like trip ID, origin, and destination.
- **Stop Management**: Add and manage stops associated with each trip. Each stop has a unique ID, and the system ensures that no stop ID is duplicated.
- **Error Handling**: Includes validation checks to prevent duplicate stop IDs and form input errors.
- **Responsive Design**: The app is built with a responsive layout, ensuring accessibility on various devices.

## Requirements

- Python 3.12 or higher
- Django 5.1.1 or higher
- Database (SQLite, PostgreSQL, etc.)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/m2bass/GTFS_project.git
   cd rideshare

2. **Set up a virtual environment**:
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

3. **Install the required dependencies**:
pip install -r requirements.txt

4. **Set up the database**:
Run the following command to apply migrations and set up your database:
python manage.py migrate

5. **Create a superuser (optional)**:
To access the Django admin panel, create a superuser account:
python manage.py createsuperuser

6. **Start the development server**:
Run the development server to view the application:
python manage.py runserver

The app should be accessible at http://127.0.0.1:8000.

**Usage**
**Trip Management**
Visit the home page to view the list of trips.
You can add new trips, update existing ones, or delete trips using the provided interface.
Each trip has a destination, origin, and other necessary information.
**Stop Management**
Each trip can have multiple stops associated with it.
You can add, update, and remove stops from a trip.
Stop IDs are unique, and the system will prevent duplicate entries.
**Admin Panel**
To access the Django admin panel for managing trips and stops:

Go to http://127.0.0.1:8000/admin.
Log in with the superuser credentials created earlier.
From here, you can manually manage trips, stops, and users.
**Configuration**
You can adjust some settings in the settings.py file located in the rideshare directory:

STATIC_URL: URL path for serving static files (CSS, JavaScript, images).
STATICFILES_DIRS: Directory paths for custom static files.
DATABASES: Configure the database settings for production (e.g., PostgreSQL or MySQL).
Development

If you wish to learn more
 https://medium.com/django-unleashed/complete-django-project-setup-a-comprehensive-guide-289182b75f3c#:~:text=Whether%20you%E2%80%99re%20a%20seasoned%20developer%20or
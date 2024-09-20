# Thought Storage App

## Overview
The Thought Storage App is a Django-based web application designed to help users store and manage their thoughts. Users can create, read, update, and delete their thoughts in a simple and intuitive interface.

## Features
- User authentication (sign up, log in, log out)
- CRUD - create, read, update, and delete thoughts
- List all thoughts
- Responsive design for mobile and desktop

## Installation

### Prerequisites
- Python 3.8+
- Django 3.2+
- pip (Python package installer)

### Steps
1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/thought-storage-app.git
    cd thought-storage-app
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Access the app:**
    Open your web browser and go to `http://127.0.0.1:8000`.

## Usage
- **Sign Up:** Create a new account to start storing your thoughts.
- **Log In:** Access your account to view and manage your thoughts.
- **Create Thought:** Add a new thought by filling out the form.
- **Edit Thought:** Update an existing thought.
- **Delete Thought:** Remove a thought from your list.


## Contact
For any questions or suggestions, please contact your-email@example.com.

## Expense Tracker – TrackMate

TrackMate is a Django-based Expense Tracker web application that helps users manage their finances efficiently. Users can track income and expenses, view summaries, and see visual reports in charts.

## Features:

1.User authentication (signup/login/logout)
2.Add, edit, and view income and expense transactions
3.Track total, maximum, and minimum income/expense
4.Visual representation with Pie and Bar charts
5.Net income calculation
6.Responsive and user-friendly dashboard

## Project Structure

expense_tracker/
│── manage.py
│── db.sqlite3
│── requirements.txt
│
├── expense_tracker/ # Project configuration
│ ├── init.py
│ ├── settings.py # Django settings
│ ├── urls.py # Project-level URLs
│ ├── wsgi.py
│ └── asgi.py
│
├── tracker/ # Main app
│ ├── migrations/ # Database migrations
│ ├── templates/tracker/ # HTML templates (dashboard, forms, history)
│ ├── static/tracker/ # CSS, JS, images
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py # Django forms
│ ├── models.py # Database models
│ ├── urls.py # App-level routes
│ └── views.py # Core logic
│
└── screenshots/ # App screenshots for README
├── homepage.png
├── dashboard.png
├── add_expense.png
└── income_history.png

## Technology Stack:

1.Backend: Python, Django
2.Frontend: HTML, CSS, JavaScript, Chart.js
3.Database: SQLite (default for Django)
4.Libraries: Chart.js for charts, Bootstrap (optional)

## Installation:

1.Clone the repository:
git clone <your-repo-link>
cd expense_tracker

2.Create and activate a virtual environment:
python -m venv venv

# Windows
venv\Scripts\activate

3.Install dependencies:
pip install -r requirements.txt

4.Apply migrations:
python manage.py migrate

5.Run the development server:
python manage.py runserver

6.Open your browser and go to:
http://127.0.0.1:8000/

## Usage:

1.Signup and login to your account
2.Add income and expense transactions
3.View your dashboard for totals, max/min values, and net income
4.Use Pie and Bar charts for visual insights

## Viewing the SQLite Database Online

This project uses **SQLite** as the database (`db.sqlite3`). You can view the database contents directly in your browser without installing anything using an **online SQLite viewer**.

### Steps:

1. Go to [SQLite Online](https://sqliteonline.com/) or [SQLite Viewer](https://inloop.github.io/sqlite-viewer/).
2. Click **Open Database** or **Choose File**.
3. Upload the `db.sqlite3` file from your project folder.
4. Browse the tables to see data such as income, expenses, and other records.

## Screenshots of TrackMate:
1.### Homepage
![Expense History Screenshot](screenshots/Homepage.png)
2.### Dashboard
![Dashboard Screenshot](screenshots/dashboard.png)
3.### Add Expense
![Add Expense Screenshot](screenshots/add_expense.png)
4.### Expense History
![Expense History Screenshot](screenshots/income_history.png)

## 🛠️ Tech Stack
- Backend: Django (Python)
- Frontend: HTML, CSS, JavaScript
- Charts: Chart.js
- Database: SQLite (default, can switch to PostgreSQL/MySQL)
 Contributing

##  Usage
This project is open for personal or educational use.  
Feel free to use, modify, and share it – no restrictions. 

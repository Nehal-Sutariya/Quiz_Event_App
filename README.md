# Quiz_Event_App



A web-based Quiz & Events Management System built using Django that allows users to participate in quizzes and view events, while the admin can manage questions, answers, users, and events from the admin panel.


------------------------------------------
Features

User Panel
- User Registration & Login
- View Available Quizzes
- Attempt Quiz
- View Results
- View Events
- Logout
------------------------------------------
Admin Panel
- Secure Admin Login
- Manage Users
- Add / Edit / Delete Quiz Questions
- Add / Edit / Delete Answers
- Create & Manage Events
- View Quiz Results

-----------------------------------------
Technologies Used

- Backend: Django (Python)
- Frontend: HTML, CSS, Bootstrap
- Database: SQLite (default)
- Authentication: Django Auth System
- Environment: Virtual Environment (venv)

----------------------------------------------------------------------------------------------------------------------------

How to work:

Step 1: Activate Virtual Environment
venv\Scripts\activate

Step 2: Install Dependencies
pip install django

Step 3: Run Migrations
python manage.py makemigrations
python manage.py migrate

Step 4: Create Superuser
python manage.py createsuperuser

Step 5: Run Server
python manage.py runserver
--------------------------------------

Open in browser:
http://127.0.0.1:8000/


Admin Panel:
http://127.0.0.1:8000/admin/


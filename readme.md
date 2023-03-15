# Django REST API Project
This is a simple Django REST API project that allows you to manage a list of students. It uses Django for backend, Class-based views for CRUD operations, and Axios for making API requests. Users can register, login, and see only the students they added to the list. Token is used for Authentication.
Also, it enables images uploading.
## Features
Django-based backend
CRUD operations using class-based views
CORS handling
Axios for API requests
User authentication (register and login)
Users can view and manage only the students they added

## Installation
1. Make sure you have Python 3.x installed on your system.
2. Clone this repository and navigate to the project root.
 - git clone <REPOSITORY_LINK>
 - cd <PROJECT_FOLDER>
3. Create a virtual environment and activate it.
 - python -m venv venv
 - source venv/bin/activate  # For Linux and macOS
 - venv\Scripts\activate  # For Windows
4. Install the required packages from the requirements.txt file.
 - pip install -r requirements.txt
5. Apply migrations to create the database schema.
 - python manage.py migrate
6. Run the development server.
 - python manage.py runserver
7. Open your web browser and visit http://127.0.0.1:8000/.


## Usage
1. Register a new user or log in with an existing account.
2. After logging in, you can see a list of students you added.
3. Add, update, or delete students using the provided form and buttons.

The API allows you to perform the following actions:
 - Get a list of all students
 - Add a new student
 - Update an existing student
 - Delete a student

## File Structure
 - views.py: Contains the views for CRUD operations, user registration, and authentication.
 - models.py: Contains the Students model.
 - index.html: The main HTML file for displaying and managing students.
 - requirements.txt: Lists the required packages for this project.

## Dependencies
Django: 4.0.6
django-cors-headers: 3.13.0
djangorestframework: 3.13.1
djangorestframework-jwt: 1.11.0
djangorestframework-simplejwt: 5.2.0
Pillow: 9.2.0
PyJWT: 1.7.1
Gunicorn: 20.1.0

You can interact with the API using a tool like Axios. For example:

### Example 1:
axios.get('http://127.0.0.1:8000/students/')
  .then(response => console.log(response.data))
  .catch(error => console.log(error));

### Example 2: 
const formData = new FormData();
formData.append("sname", "John Doe");
formData.append("age", "25");
formData.append("email", "johndoe@example.com");

axios.post('http://127.0.0.1:8000/students/', formData)
  .then(response => console.log(response.data))
  .catch(error => console.log(error));


### Example 3:
const formData = new FormData();
formData.append("sname", "John Doe");
formData.append("age", "26");
formData.append("email", "johndoe@example.com");

axios.put('http://127.0.0.1:8000/students/1/', formData)
  .then(response => console.log(response.data))
  .catch(error => console.log(error));


### Example 4:
axios.delete('http://127.0.0.1:8000/students/1/')
  .then(response => console.log(response.data))
  .catch(error => console.log(error));

# netlify (site):
https://visionary-figolla-deb19e.netlify.app/

# render (back):
https://django-classcrud-login-register-user-html.onrender.com/


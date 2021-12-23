# The Link

## Setup for Windows

#### In the backend folder, run the following commands to start the django server at http://localhost:8000 -
- `pip install virtual env`
- `virtualenv env`
- `env\Scripts\activate`
- `pip install -r requirements.txt`
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py createsuperuser` - enter username and password after this command. (Email is optional and can be left blank)
(set the admin username as ***@thapar.edu** to be able to login from the main page)
- `python manage.py runserver`

#### - From the login page, you can register as a student only.
#### - For admin login, go to http://localhost:8000/admin/
#### - Create a teacher account from the admin page under the users section, make sure to **check the teacher status box** and **add a faculty code** for functionalities to work. Also make sure to set the username as ***@thapar.edu** else you login from the main login page will be restricted.

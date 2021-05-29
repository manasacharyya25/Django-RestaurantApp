Commands:

- python -V -- Python Version
- python3 -V -- Python 3 Version 
- virtualenv . -- Create a Virtual Environment in Current DIrectory (.) 
- .Scripts\activate -- Activate Virtual Environment
- pip install django==2.0.7 -- Install Django 
- pip freeze --  See all installed packages in current env
- django-admin -- Work on all sots of command with django
- django-admin startproject <project-name> . -- Create Django Project in Current Directory(.)
- python manage.py runserver -- Run Django Project 
- python manage.py migrate --  Sets up Django Project with built in sqllite db
- python manage.py createsuperuser  -- Required to access Admin @localhost:8000/admin
- python manage.py startapp <appname> -- Create Apps (Components) of the Project 
- python manage.py makemigrations -- To be called each time a change is made to project
- python manage.py shell 


Create and Register New App (Component of Project)

1. python manage.py startapp <component_name>  --- This will create a dir with component name, that will hold all code for                                                                                                                             that component
2.  Add Code for that Component
3.  Add component name in settings.py > INSTALLED_APPS
4.  python manage.py makemigrations
5.  python manage.py migrate
6.  In admin.py -> from .models.py import <Component_Name>
				admin.site.register(<Component_Name>)




Notes:

- In root directory of a Django Project, there is a manage.py file.
  
- Another folder is the one with name of the project. That stores all codes for the project.
  
- settings.py is a file in project directory, which stores all settings of the django project 
  
  

# Web Dev with Django Rest Framework
## Contents
- Dev Environment Setup
- Django Basics
- REST API with DRF

## Dev Environment Setup
- **IDE** Pycharm Community Edition ( Provides Intellisense for Django and DRF Code )
- **Python Version**  Python 3.7.8
- **Create Python Virtual Environment**
	```
	virtualenv .
	``` 
- **Activate Python Virtual Environment**
	```
	Scripts\activate
	```
- **Install Django**
	```
	pip install django==3.2.3
	```
- **Install Django Rest Framework**
	```
	pip install djangorestframework==3.12.4
	```
- **Check Installed Packages**
	```
	pip freeze
	```

## Django Basics

### Setup Project Skeleton

- Before Starting any Django Project, create a ```src``` folder, that will contain all Project Files.

- **Create Django Project**
	```
	... activate virtual env ...
	
	> cd src
	> django-admin startproject <project-name> .
	```
	Creates a folder called ```<project-name>``` with following contents:
	-	project-name 
         -  project-name
			-	init.py
			-	asgi.py
			-	settings.py
			-	urls.py
			-	wsgi.py
		-	manage.py
		-					
- **Create a component**  of the Project. (Called App in Django Terms)
	```
	... activate virtual env ...
	
	> cd src\<project-name>
	> python manage.py startapp <app-name>
	> django-admin startapp <app-name> .
	```
	Creates a folder called ```<app-name>```  with following contents:
	-	migrations/
	-	init.py
	-	admin.py
	-	apps.py
	-	models.py
	-	tests.py
	-	views.py

- **Register Component** in Project Settings
	- Opne src\project-name\project-name\settings.py
	- Under ```INSTALLED_APPS``` add ```'app-name'```

- While we are at it, include ```rest-framework``` as well under `INSTALLED_APPS``` that was installed during dev env setup phase.

- **Create Superuser**
	Django allows creating a superuser with name, email and password. Using these credentials one can login into admin panel and access secure content within the webapp.

	To create a superuser, execute following in terminal:
	
	```
	> cd src\project-name
	> python manage.py createsuperuser
	```
	
	This should prompt to update username, email and password. Fill in details and continue.


-	**Start Django Server**

	```
	> cd src\project-name
	> python manage.py runserver
	```

- The Django server would by default start at ```http:\\localhost:8000```
	Navigate to ```http:\\localhost:8000\admin```. Type in username and password, that was set in previous step and you should be in the Admin Dashboard.


### Django Coding
Developing any Django Applicaton, would require the follwing steps to be performed :
	1. Create **Model** classes - The Data Models to store data

```
from django.db import models  
 
class Menu(models.Model):  
    created = models.DateField(auto_now_add=True)  
    item_name = models.TextField(max_length=10)  
    item_price = models.IntegerField()  
  
    class Meta:  
        ordering = ['created']
```

2.**Serializers** for that Model - To Serialize and Deserialize models to/from JSON

```
from rest_framework import serializers  
from .models import Menu  
  
  
class MenuSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Menu  
        fields = ['created', 'item_name', 'price']
```

 3.  **Migrating Model Changes to DB** - Create Schema for Models in DB

```
> python manage.py makemigrations
> python manage.py migrate
```

4. **Registering Model into Admin** -  Allow easy manipulation of Models from Django Admin UI

```
from django.contrib import admin  
from .models import Menu  

admin.site.register(Menu)
```

		 
## REST API with DRF

- To Create a REST API, in addition to Models and Serializers created in previous step, we also need to create **Views** ( similar to controller ) and **URL Mappings** ( api endpoints ) to these. 

	1. **View Class** : Using Generics provided by rest_framework, we can avoid boilerplate code required to setup GET, POST, PUT, DELETE APIs

		```
		from rest_framework import generics  
		from .models import Menu  
		from .serializers import MenuSerializer
		  
		class MenuView(generics.ListAPIView):  
		    queryset = Menu.objects.all()  
		    serializer_class = MenuSerializer
		```

	2. **URL Configuration**: Create ```urlpatterns``` in ```app.urls.py``` and Include that in ```project -> settings.py -> urlpatterns```

		```
		from django.urls import path  
		from .views import SnippetsList  
		from rest_framework.urlpatterns import format_suffix_patterns  
		  
		  
		urlpatterns = [  
		    path('snippets/', SnippetsList.as_view())  
		]  
		  
		urlpatterns = format_suffix_patterns(urlpatterns)

		```

		```
		from django.contrib import admin  
		from django.urls import path, include  
		  
		urlpatterns = [  
		    path('admin/', admin.site.urls),  
		  path('', include('Menu.urls'))  
		]
		```

- Also we need to change default **RENDERED and PARSER** Classes, so that we get JSON Response when accessing the APIs. 
Add following to ```project->settings.py```

		```
		REST_FRAMEWORK = {  
		    'DEFAULT_RENDERER_CLASSES': [  
		        'rest_framework.renderers.JSONRenderer',  
		  ],  
		  'DEFAULT_PARSER_CLASSES': [  
		        'rest_framework.parsers.JSONParser',  
		  ]  
		}
		```
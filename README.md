# BlogsDjango


This project used class-based view, form, and model forms.


# To setup 

## Create virtualenv and install require packages


    python -m venv virtualenv

    .\virtualenv\Scripts\activate

    pip install -r .\requirements.txt


## Setup db in MySQL


    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'db_dev_blogs_django',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': '127.0.0.1',
            'PORT': '3306',
        }
    }


Run Migration commands

    python manage.py migrate


## Create superuser

    python manage.py createsuperuser



## Add Django toolbox
1. Link: https://www.tutorialspoint.com/how-to-add-django-debug-toolbar-to-your-project

Django toolbox is a debugging tool that is **used to debug database queries, 
Django website loading speed, and many other things**. 

- Install 


    pip install django-debug-toolbar


-  add 'debug_toolbar' to your INSTALLED_APPS in settings.py


    INSTALLED_APPS = [
       # ...
       'debug_toolbar',
       'blogs_django.accounts'
    ]


- Add middleware in settings.py


    MIDDLEWARE = [
       # ...
       'debug_toolbar.middleware.DebugToolbarMiddleware',
       # ...
    ]


- Now, in settings.py, add one more variable INTERNAL_IPS and mention localhost in it 


    INTERNAL_IPS = [
       '127.0.0.1',
    ]


- urls.py of your project main directory, add the debug toolbar url
    


## Send Mail
1. Link :- https://pypi.org/project/django-templated-email/


- settings.py


    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


---


    TEMPLATED_EMAIL_TEMPLATE_DIR = 'templated_email/'
    TEMPLATED_EMAIL_FILE_EXTENSION = 'html'

